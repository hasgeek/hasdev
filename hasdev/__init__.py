import os
from yaml import load

apps = load(file('instance/apps.yml', 'r'))
settings = load(file('instance/settings.yml', 'r'))

def clone(app):
	try:
		os.chdir(settings['options']['apps_path'])
		if not os.path.exists("%s/.git" % app):
			print "Cloning %s..." % app
			os.system('date >> ../logs/git.log; git clone %s >> ../logs/git.log' % (settings['options']['repo_url'] % app))
		os.chdir("..")
	except KeyboardInterrupt:
		print "Cloning interrupted. Removing %s..." % app
		os.system('rm -rf %s' % app)
		os.chdir("..")
		print "Removed %s..." % app
		exit()

def setup(app):
	app_path = "%s/%s" % (settings['options']['apps_path'], app)
	remote_app_path = "/vagrant/%s" % app_path
	try:
		print "Setting up %s for development..." % app
		run(app, "sudo python setup.py develop")
	except KeyboardInterrupt:
		print "Setup interrupted. Removing %s..." % app
		os.system('rm -rf %s' % (app_path))
		exit()

def install(app):
	if app == "all":
		for app in apps:
			if 'dev_setup' not in apps[app] or apps[app]['dev_setup'] is False:
				install(app)
	elif app in apps and 'dev_setup' in apps[app] and apps[app]['dev_setup']:
		print "Installing %s..." % app
		clone(app)
		setup(app)
	elif app in apps and ('dev_setup' not in apps[app] or apps[app]['dev_setup'] is False):
		print "Installing %s..." % app
		clone(app)
		update_requirements(app)
	else:
		print "%s not configured"

def update(app):
	pull(app)
	update_requirements(app)

def pull(app):
	path = "%s/%s" % (settings['options']['apps_path'], app)
	if os.path.exists(path):
		os.chdir(path)
		os.system("date >> ../logs/git.log; git pull >> ../logs/git.log;")
		update_requirements(app)
		os.chdir("../..")
	else:
		print "App does not exist..."

def update_requirements(app):
	print "Setting up requirements..."
	if os.path.exists("%s/%s/requirements.txt" % (settings['options']['apps_path'], app)):
		run(app, "sudo pip install -r requirements.txt --upgrade")
	else:
		print "requirements.txt not found for %s" % app

def run(app, command):
	path = "%s/%s" % (settings['options']['apps_path'], app)
	if os.path.exists(path):
		remote_app_path = "/vagrant/%s" % path
		command = "cd %s; %s" % (remote_app_path, command)
		os.system("vagrant ssh -c 'date >> /vagrant/logs/remote-commands.log; echo \"%s\" >> /vagrant/logs/remote-commands; %s >> /vagrant/logs/remote-commands'" % (command, command))
	else:
		print "App does not exist..."

def init():
	choice = ""
	YN = {"yes":True, "y":True, "ye":True, "no":False, "n":False}
	while choice not in YN:
		choice = raw_input("Do you want to setup all apps after the VM is created and setup[y/n]? ").lower()
	if not os.path.exists(settings['options']['apps_path']):
		print "Directory %s doesn't exist. Creating %s..." % settings['options']['apps_path']
		os.mkdir(settings['options']['apps_path'])
	if not os.path.exists(".vagrant/machines/default/virtualbox/id"):
		print "Setting up virtual machine..."
		os.system("vagrant up --provision")
	else:
		print "Virtual machine already exists..."
	for app in apps:
		if 'dev_setup' in apps[app] and apps[app]['dev_setup'] and not os.path.isdir("%s/.git" % app):
			install(app)
	if YN[choice]:
		install("all")