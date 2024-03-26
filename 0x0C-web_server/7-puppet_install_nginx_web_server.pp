# Setup Ubuntu Server with nginx

exec { 'system_update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['system_update'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    location = / {
        root /var/www/html;
    }
    location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
    }
}',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
