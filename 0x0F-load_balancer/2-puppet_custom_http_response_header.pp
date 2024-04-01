# Setup Ubuntu Server with nginx

exec { 'command':
  command  => 'apt-get update; \
               apt-get install nginx -y; \
               echo "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" | sudo tee /etc/nginx/sites-available/default; \
               service nginx restart',
  provider => shell,
}
