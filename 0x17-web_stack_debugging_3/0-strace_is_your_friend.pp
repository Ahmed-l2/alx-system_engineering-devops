# Puppet manifest to replace occurrences of "phpp" with "php" in /var/www/html/wp-settings.php

exec { 'replace_phpp_with_php':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php',
  path    => '/bin','/usr/bin'
}
