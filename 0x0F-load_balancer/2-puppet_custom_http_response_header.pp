# Setup Ubuntu Server with nginx

exec { 'update server':
  command  => 'sudo apt-get update',
  provider => 'shell',
}

package { 'nginx':
  ensure   => present,
}

file_line { 'HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
