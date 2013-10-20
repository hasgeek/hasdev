# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'
settings = YAML::load_file('instance/settings.yml')
apps = YAML::load_file('instance/apps.yml')

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  
  apps.each do |app, opts|
    if opts['port']
      config.vm.network :forwarded_port, guest: opts['port'], host: opts['port']
    end
  end
  
end
