# updates the ULIMIT value in /etc/default/nginx to 4096 and restarts the NGINX service if the value is changed.

exec { 'nginx-ulimit':
  command => '/bin/sed -i "s/ULIMIT=\"-n [0-9]*\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['nginx-ulimit'],
}
