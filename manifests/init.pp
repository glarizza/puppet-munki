class puppet_munki {
  file { '/usr/local/munki/munki_do.py':
    ensure => file,
    mode   => '0700',
    owner  => '0',
    group  => '0',
    source => 'puppet:///modules/puppet-munki/munki_do.py',
  }
}
