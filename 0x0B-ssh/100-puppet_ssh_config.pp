#!/usr/bin/env bash
#Using puppet to conenct to ssh server without password

file { '/etc/ssh/sshd_config'
  ensure  => present,
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
