# executes the command pkill on the process killmenow

exec { 'pkill -f killmenow':
    path   => 'usr/bin/:/usr/local/bin/:/bin/',
    onlyif => 'test `pgrep -f killmenow | wc -l` -gt 0',
}
