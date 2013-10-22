# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'
settings = YAML::load_file('instance/settings.yml')
apps = YAML::load_file('instance/apps.yml')

VAGRANTFILE_API_VERSION = "2"

app_hosts = []

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.network :private_network, ip: settings['vm']['host_ip']
  config.vm.hostname = settings['vm']['hostname']

  apps.each do |app, opts|
    if opts['port']
      config.vm.network :forwarded_port, guest: opts['port'], host: opts['port']
      if opts['host']
        app_hosts.push(opts['host'])
      else
        app_hosts.push(settings['options']['base_host'] % app)
      end
    end
  end

  config.vm.provision "shell", path: "hasdev/init.sh"

  # Adding /etc/hosts entries, `vagrant plugin install vagrant-hostsupdater`
  if defined? VagrantPlugins::HostsUpdater
    config.hostsupdater.aliases = app_hosts
  else
    puts "vagrant-hostsupdater not installed, so not updating /etc/hosts"
  end

end
