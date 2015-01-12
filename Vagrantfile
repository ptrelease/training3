# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "landregistry/ubuntu"
  config.vm.provision :shell, path: "provision.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 5555  
end
