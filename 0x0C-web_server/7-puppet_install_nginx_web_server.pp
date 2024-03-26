# Setup Ubuntu Server with nginx

exec { 'system_update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['system_update'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80;
      root /var/www/html;
      index index.html index.htm;


      location = / {
        return 200 'Hello World!';
      }

      location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
      }
    }
  ",
  notify  => Service['nginx'],
}
