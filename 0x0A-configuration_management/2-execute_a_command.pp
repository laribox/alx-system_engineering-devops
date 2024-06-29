# Terminate all processes named killmenow

exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }