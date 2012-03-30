#!/usr/bin/python
# encoding: utf-8
#
# Copyright 2009-2012 Greg Neagle.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
munki_do
"""
import optparse
import subprocess
import sys

from munkilib import FoundationPlist
from munkilib import updatecheck
from munkilib import installer
from munkilib import munkicommon

p = optparse.OptionParser()
p.add_option('--catalog', '-c', action="append",
           help='Which catalog to consult. May be specified multiple times.')
p.add_option('--install', '-i', action="append",
           help='An item to install. May be specified multiple times.')
p.add_option('--uninstall', '-u', action="append",
           help='An item to uninstall. May be specified multiple times.')
p.add_option('--checkstate', action="append",
           help='Check the state of an item. May be specified multiple times.')

options, arguments = p.parse_args()
cataloglist = options.catalog or ['production']

if options.checkstate:
   updatecheck.MACHINE = munkicommon.getMachineFacts()
   updatecheck.CONDITIONS = munkicommon.getConditions()
   updatecheck.getCatalogs(cataloglist)
   for check_item in options.checkstate:
       installed_state = 'unknown'
       item_pl = updatecheck.getItemDetail(check_item, cataloglist)
       if item_pl:
           if updatecheck.installedState(item_pl):
               installed_state = "installed"
               exit_code = 0
           else:
               installed_state = "not installed"
               exit_code = 1
       print "%s: %s" % (check_item, installed_state)
       exit(exit_code)

if not options.install and not options.uninstall:
   exit()

manifest = {}
manifest['catalogs'] = cataloglist
manifest['managed_installs'] = options.install or [] 
manifest['managed_uninstalls'] = options.uninstall or [] 
FoundationPlist.writePlist(manifest, '/tmp/localmanifest.plist') 
updatecheckresult = updatecheck.check( 
    localmanifestpath='/tmp/localmanifest.plist') 
if updatecheckresult == 1: 
  need_to_restart = installer.run() 
  if need_to_restart: 
    print "Please restart immediately!" 
