#!/usr/bin/env python
import os
import sys
from yaml import load
import hasdev

apps = load(file('instance/apps.yml', 'r'))
settings = load(file('instance/settings.yml', 'r'))

if __name__ == "__main__":
    args = sys.argv
    while len(args) < 3:
        args.append(None)
    
    if args[1] == 'init':
        hasdev.init()
    elif args[1] == 'install':
        hasdev.install(args[2])
    elif args[1] == 'update':
        hasdev.update(args[2])
    else:
        print "Invalid command"