include puppet-munki

munki_package { 'Firefox':
  ensure  => present,
  catalog => 'production',
}
