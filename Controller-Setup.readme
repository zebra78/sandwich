# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.define "centos" do |centos|
        centos.vm.box 		                = "hashicorp-vagrant/centos-7.4"
        centos.ssh.username 	            = "vagrant"
        centos.ssh.password 	            = "vagrant"
        centos.ssh.insert_key 	          = false
        centos.ssh.forward_agent          = true
        centos.vm.hostname 	              = "ctrlr.ubuntu.com"
        centos.vm.network 	              "private_network", ip: "192.168.100.4"
    end
    config.vm.define "webserver1" do |webserver1|
        webserver1.vm.box 		            = "hashicorp-vagrant/centos-7.4"
        webserver1.ssh.username 	        = "vagrant"
        webserver1.ssh.password 	        = "vagrant"
        webserver1.ssh.insert_key         = false
        webserver1.ssh.forward_agent      = true
        webserver1.vm.hostname 	          = "webserver1.ubuntu.com"
        webserver1.vm.network 	          "private_network", ip: "192.168.100.5"
    end
end


