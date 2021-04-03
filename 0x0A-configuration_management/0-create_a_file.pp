#Using Puppet, create a file in /tmp.
#
#Requirements:
#
#File path is /tmp/holberton
#File permission is 0744
#File owner is www-data
#File group is www-data
#File contains I love Puppet

file { "/tmp/holberton":
	path => "/tmp/holberton",
	mode => "0744",
	owner => "www-data",
	group => "www-data",
	content => "I Love Puppet",
}
