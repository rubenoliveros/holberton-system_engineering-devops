#Using Puppet, install puppet-lint.
#
#Requirements:
#
#Install puppet-lint
#Version must be 2.1.1

package { 'puppet-lint':
  ensure   => '2.1.1',
	provider => 'gem',
}
