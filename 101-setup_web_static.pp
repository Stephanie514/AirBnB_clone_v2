# Puppet manifest to set up web servers for the deployment of web_static

# Update package list and install Nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Holberton School</p>
  </body>
</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Change ownership
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
}

# Create directories for /var/www
file { '/var/www':
  ensure => 'directory',
}

file { '/var/www/html':
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Holberton School</p>
  </body>
</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Update Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'present',
  content => template('path/to/nginx_config.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
