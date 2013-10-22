# hasdev

Virtual development environment for HasGeek apps using Vagrant.

## Installation Prerequisites
* The SSH key for the host machine should be added on github; git will be used on the host machine
* Python
* Virtualbox
* Vagrant
* `vagrant plugin install vagrant-hostsupdater`

## Setup Instructions
* Address the prerequisites
* Clone repo to a location where you want to store your applications
* Go to root directory
* Run `python manage.py init`

## Usage Notes
`manage.py` gives you an interface to do various things with the virtual machine.

### init
`python manage.py init`

This is supposed to be run to initialise the environment.

It handles the following:
* Creates the VM, if it does not exist
* Runs the provisioning script
* Clones and sets up a few app dependencies, viz. coaster, baseframe
* All repositories are cloned into the `apps` directory under hasdev root
* As per your response to the initial prompt, it also clones and installs all configured HasGeek apps

It is run only for the first time and will not be required after you setup your VM once. You will need to run this each time your destroy your VM.

### install
`python manage.py install --app=<app_name>`

Installs a given HasGeek app, if it is configured in `instance/apps.yml`.

Running this will also run `sudo pip install -r requirements.txt --upgrade`, if the `requirements.txt` file exists for an app.

You can run `python manage.py install --app=all` to install all configured HasGeek apps.

### update
`python manage.py update --app <app_name>`

Does a git pull and then runs `sudo pip install -r requirements.txt --upgrade`, if the `requirements.txt` file exists for an app.

### run
`python manage.py run --app <app_name> --execute "<provided_command>"`

CDs to the `app_name` directory & runs the `provided_command`.

E.g. usage:

* `python manage.py run --app nodular --execute "nosetests"`

### provision
`python manage.py provision`
Equivalent to running `vagrant provision`

## To-dos
* Database setups in `python manage.py install`