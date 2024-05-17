# Increase file limits for Holberton user.

exec { 'increase-holberton-file-limits':
  command => "sed -i '/^holberton/s/\(soft\|hard\) nofile [0-9]*/\\1 nofile 50000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin', '/bin'],
}
