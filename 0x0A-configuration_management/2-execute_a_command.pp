# Using puppet to kill a process named killmenow.

exec { 'pkill -f killmenow':
  path => 'usr/bin/:/usr/local/bin/:/bin/'
}