import os
from .helpers import *

def clone(app):
    make_parent(app)
    os.chdir(apps[app]['type'])
    if not os.path.exists("%s/.git" % app):
        print "Cloning %s..." % app
        os.system('git clone %s' % (settings['options']['repo_url'] % app))
    if 'branch' in apps[app]:
        os.chdir(app)
        os.system("git checkout %s" % apps[app]['branch'])
        os.chdir("..")
    os.chdir("..")

def setup(app):
    print "Setting up %s for development..." % app
    command = []
    if app == 'baseframe':
        command.append("sudo pip install webassets==0.8")
    command.append("sudo python setup.py develop")
    if app == 'baseframe':
        command.append("cd baseframe")
        command.append("make")
    run(app, ";".join(command))

def install(app):
    if app == "all":
        for app in apps:
            if apps[app]['type'] is not "dependencies":
                install(app)
    elif app in apps:
        print "Installing %s..." % app
        clone(app)
        if apps[app]['type'] == "dependencies":
            setup(app)
        elif apps[app]['type'] != "boilerplates":
            update_requirements(app)
        if 'db' in apps[app] and apps[app]['db']:
            print "Creating database %s..." % app
            command = "sudo -u postgres createdb %s;" % app.replace(".", "")
            command = "%s sudo -u postgres psql -c \"GRANT ALL ON DATABASE %s TO hasgeek\"" % (command, app)
            os.system("vagrant ssh -c '%s'" % command)
    else:
        print "%s not configured"

def update(app):
    if app == "all":
        for app in apps:
            update(app)
    pull(app)
    if apps[app]['type'] == "dependencies":
        setup(app)
    elif apps[app]['type'] != "boilerplates":
        update_requirements(app)

def pull(app):
    if os.path.exists(dir(app)):
        print "Updating %s..." % app
        os.chdir(dir(app))
        os.system("git pull")
        os.chdir("../..")
    else:
        print "App %s does not exist..." % app

def update_requirements(app):
    print "Setting up requirements..."
    if os.path.exists("%s/requirements.txt" % dir(app)):
        run(app, "sudo pip install -r requirements.txt --upgrade")
    else:
        print "requirements.txt not found for %s" % app

def init():
    choice = ""
    YN = {"yes":True, "y":True, "ye":True, "no":False, "n":False}
    while choice not in YN:
        choice = raw_input("Do you want to setup all apps after the VM is created and setup[y/n]? ").lower()
    if not os.path.exists(".vagrant/machines/default/virtualbox/id"):
        print "Setting up virtual machine..."
        os.system("vagrant up --provision")
    else:
        print "Virtual machine already exists..."
    for app in apps:
        if apps[app]['type'] == "dependencies":
            install(app)
    if YN[choice]:
        install("all")