# kill process killmenow

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  user    => 'root',
}
