#!/bin/bash
# Update package list and install Nginx
#Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared,current}

sudo echo "<html>
 <head>
 </head>
 <body>
   Holberton School
 </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_update="location /hbnb_static {\n    alias /data/web_static/current/;\n}"
sudo sed -i "/listen 80 default_server/a $config_update" /etc/nginx/sites-enabled/default

# Restarting Nginx
sudo service nginx restart
