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
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
