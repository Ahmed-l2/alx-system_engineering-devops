#puppet manifest to install nginx and setup 301 redirect

# Class: nginx
# This class installs and manages the Nginx service.
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

include nginx
