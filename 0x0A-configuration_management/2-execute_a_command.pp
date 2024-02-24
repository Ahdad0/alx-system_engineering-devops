# Execute a command using puppet
# Made by MEGA

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}
