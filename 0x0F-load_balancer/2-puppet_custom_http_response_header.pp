#This manifest creates a custom HTTP header response

include stdlib

exec { 'update system':
  provider => shell,
  command  => 'apt-get update -y',
  before   => Package['nginx'],
}

Package { 'nginx':
  ensure => installed,
  before => File_line['add-header'],
  notify => Service['nginx']
}

file_line { 'add_header':
  ensure => present,
  line   => '        add_header X-Served-By $hostname always;',
  after  => '^http {',
  path   => '/etc/nginx/nginx.conf',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
}
