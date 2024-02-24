# kill a running process

exec { 'killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}
