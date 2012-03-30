include puppet-munki

munki_package { 'Firefox':
  ensure  => present,
  catalog => 'production',
  require => Class['puppet-munki'],
}
