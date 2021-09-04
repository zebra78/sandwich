# -*- mode: ruby -*-
# vi: set ft=ruby :

#POST INSTALL alias aws="python3 -m awscli"
$bootstrap=<<SCRIPT
  apt-get update
  apt-get install python3-pip -y
  su -c 'pip3 install awscli --upgrade --user' vagrant
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.define "awscli" do |a|
    a.vm.box                      = "bento/ubuntu-18.04"
    a.vm.hostname                 = "awscli2.ubuntu.com"
    a.vm.network                  "private_network", ip: "192.168.100.169"
    a.vm.provision                :shell, inline: $bootstrap
  end

  config.vm.define "proxy" do |a|
    a.vm.box                      = "bento/ubuntu-18.04"
    a.vm.hostname                 = "proxy.ubuntu.com"
    a.vm.network                  "private_network", ip: "192.168.100.170"
  end  
end


