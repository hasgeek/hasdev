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

### Commands
#### init
`python manage.py init`

This is supposed to be run to initialise the environment.

It handles the following:
* Creates the VM, if it does not exist
* Runs the provisioning script
* Clones and sets up dependencies(`python setup.py develop`)
* All repositories are cloned into their relevant directory under hasdev root
* As per your response to the initial prompt, it also clones and installs all configured HasGeek apps

It is needed to be run only for the first time and will not be required after you setup your VM once. You will need to run this each time you destroy the VM and want to set it up again.

#### install
`python manage.py install app_name`

It handles the following:
* Clones app_name, if it is configured in `instance/apps.yml`.
* Runs `sudo pip install -r requirements.txt --upgrade`, if the `requirements.txt` file exists for the app
* If a database is required for an app, it creates the database

You can run `python manage.py install all` to check out and install all configured HasGeek apps with one command.

#### update
`python manage.py update app_name`

Does a git pull and then runs `sudo pip install -r requirements.txt --upgrade`, if the `requirements.txt` file exists for an app.

### Accessing the VM
* You can go to the root folder and run `vagrant ssh` to log into the VM
* The root folder of hasdev is synced with the `/vagrant` directory inside the VM

### Apps
* Apps are located in their respective directories in `/vagrant/app_type/app`
* Go to the app directory
* Here, you can undertake all actions as specified by the respecive app, like setting it up, running the app, running tests, etc

P.S. Version control tasks should be run on the host machine