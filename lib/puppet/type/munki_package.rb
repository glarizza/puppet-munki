Puppet::Type.newtype(:munki_package) do
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


