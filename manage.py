#!/usr/bin/env python
import os
import sys
import argparse
from yaml import load
import hasdev

apps = load(file('instance/apps.yml', 'r'))
settings = load(file('instance/settings.yml', 'r'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage your development setup')
    parser.add_argument('command', help='Command to be run. Supported commands: init, install, update, run, provision')
    parser.add_argument('--app', help='The app to take a particular action on. Works with run, install & update.')
    parser.add_argument('--execute', help='The command to be executed remotely. Works with run.')
    args = parser.parse_args()
    
    if args.command == 'init':
        hasdev.init()
    elif args.command == 'install':
        hasdev.install(args.app)
    elif args.command == 'update':
        hasdev.update(args.app)
    elif args.command == 'run':
        hasdev.run(args.app, args.execute)
    elif args.command == 'provision':
        os.system("vagrant provision")
    else:
        print "Invalid command"