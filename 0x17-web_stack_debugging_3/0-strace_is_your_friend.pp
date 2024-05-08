# Puppet manifest to replace occurrences of "phpp" with "php" in /var/www/html/wp-settings.php

file_line { 'replace_phpp_with_php':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  match  => '^.*phpp.*$',
}
