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
  require => Package['nginx'],
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
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
