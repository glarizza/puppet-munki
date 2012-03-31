include puppet_munki

munki_package { 'Firefox':
  ensure  => present,
  catalog => 'production',
  require => Class['puppet_munki'],
}
