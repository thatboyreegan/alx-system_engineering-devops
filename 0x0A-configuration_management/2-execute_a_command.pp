# executes the command pkill on the process killmenow

exec { 'pkill -f killmenow':
    path => 'usr/bin/:/usr/local/bin/:/bin/'
}
