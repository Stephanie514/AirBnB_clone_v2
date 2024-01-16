#!/usr/bin/python3
"""
This fabfile distributes an archive to my web servers
"""

import os
from fabric.api import *
from datetime import datetime

# Set the host IP addresses for web-01 && web-02
env.hosts = ['35.153.79.4', '54.237.8.203']
env.user = "ubuntu"


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # Obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct path where archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(now)

    # Use fabric function to create directory if it doesn't exist
    local("mkdir -p versions")

    # Use tar command to create a compressed archive
    archived = local("tar -cvzf {} web_static".format(archive_path), capture=True)

    # Check archive creation status
    if archived.return_code != 0:
        print("Error creating archive:", archived.stdout)
        return (1)
    else:
        return (0)


def do_deploy(archive_path):
    """Deploy an archive to web servers."""
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return (0)
    return (1)


def deploy():
    """
    Create an archive and get its path, then deploy it
    """
    archive_path = do_pack()
    if archive_path != 0:
        return (1)
    return do_deploy(archive_path)
