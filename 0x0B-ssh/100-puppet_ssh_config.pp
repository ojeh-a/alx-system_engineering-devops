# Changes SSH config file

exec {'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "  IdentityFile ~/.ssh/school\n  Password no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
