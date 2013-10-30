#!/usr/bin/env python

import sys
from yaml import load
from hasdev.settings import apps, settings

marker = "#" + "*===" * 10 + "\n"

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
			hosts.write(" ".join(app_hosts) + "\n")
			print "hosts file updated..."
except Exception as e:
	print "Error: %s" % e