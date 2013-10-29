#!/usr/bin/env python

import sys
from yaml import load

marker = "#" + "*===" * 10 + "\n"
apps = load(file('/vagrant/instance/apps.yml', 'r'))
settings = load(file('/vagrant/instance/settings.yml', 'r'))

lines = []
with open("/etc/hosts", 'r') as hosts:
	for line in hosts:
		if line == marker:
			break
		lines.append(line)

app_hosts = ['127.0.0.1']
for app in apps:
	if 'port' in apps[app]:
		app_hosts.append(settings['options']['base_host'] % app)

try:
	with open("/etc/hosts", 'w') as hosts:
		hosts.write("".join(lines))
		hosts.write(marker)
		if len(app_hosts) > 1:
			print "Writing new hosts file..."
			hosts.write(" ".join(app_hosts) + "\n")
			print "Written new hosts file..."
except Exception as e:
	print "Error: %s" % e