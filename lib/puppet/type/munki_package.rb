Puppet::Type.newtype(:munki_package) do
  desc 'This is a type that will use Munki to install a package:

    munki_package { \'Firefox\':
      ensure  => present,
      catalog => \'production\',
    }

    It will use the munki_do.py script to do its work, but you must have
    an existing Munki setup and /Library/Preferences/ManagedInstalls MUST
    point back to your existing Munki server.'

  ensurable

  newparam(:name, :namevar => true) do
    desc 'The package name as known to Munki'
  end
  newparam(:catalog) do
     desc 'The catalog from which we will get the package'
     defaultto 'production'
  end
  newproperty(:version) do
    desc 'The version of the package to install'
    newvalues(/^\w+$/)
  end
end


