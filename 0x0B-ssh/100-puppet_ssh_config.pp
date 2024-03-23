#Using puppet to conenct to ssh server without password
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
