## Puppet-munki Module

This was more of a dare than anything.  Greg came up with 'munki\_do.py' that will interact with a Munki server.  This module was a response to that.  A couple of notes:

1. This is not ideal. I've created a custom type called 'munki\_package' only because I didn't want to Monkeypatch the existing 'package' type in a module.  Treat this solely as a "See? It works" prototype.
2. See note 1.

To use it, you will need to include the puppet-munki class that will create /usr/local/munki/munki\_do.py, and then declare a Munki package like so:

    munki_package { 'Firefox':
      ensure  => present,
      catalog => 'production',
    }

Godspeed.

