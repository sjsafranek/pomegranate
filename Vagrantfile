# -*- mode: ruby -*-
# vi: set ft=ruby :

# DeoDjango Vagrant Box
# https://github.com/david-wilson/vagrant-geodjango-base

# VM Customized Settings
$CPUS              = 1
$MEMORY            = 512



$update_systemd = <<SCRIPT
cat > /etc/systemd/system/pomegranate.service <<-EOF
[Unit]
Description=The Pomegranate Server

[Service]
TimeoutStartSec=10
RestartSec=10
ExecStart=/usr/bin/python3 /vagrant/manage.py runserver 0.0.0.0:8080
WorkingDirectory=/vagrant
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

systemctl enable pomegranate.service
systemctl daemon-reload
systemctl start pomegranate.service
SCRIPT



# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

#Vagrant::Config.run do |config|
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	# Base box to build off, and download URL for when it doesn't exist on the user's system already
	#config.vm.box = "ubuntu/trusty32"
	config.vm.box = "debian/jessie64"
	
	# Boot with a GUI so you can see the screen. (Default is headless)
	# config.vm.boot_mode = :gui
	
	# Assign this VM to a host only network IP, allowing you to access it
	# via the IP.
	# config.vm.network "33.33.33.10"
	
	# Forward a port from the guest to the host, which allows for outside
	# computers to access the VM, whereas host only networking does not.
	#config.vm.network :forwarded_port, guest: 8080, host: 8080
	config.vm.network "private_network", ip: "172.20.0.10", netmask: "255.240.0.0", :mac => "08002719318B"
	
	# Share an additional folder to the guest VM. The first argument is
	# an identifier, the second is the path on the guest to mount the
	# folder, and the third is the path on the host to the actual folder.
	#config.vm.share_folder "project", "/home/vagrant/{{ project_name }}", "."
	
	# Enable provisioning with a shell script.
	# sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
	config.vm.provision "shell", inline: 'aptitude update'
	config.vm.provision "shell", inline: 'aptitude -yy install install libgeos++ binutils libproj-dev gdal-bin curl htop python3-pip python3-gdal python3-jinja2'
	config.vm.provision "shell", inline: 'pip3 install django'
	config.vm.provision "shell", inline: $update_systemd
	config.vm.provision "shell", run: "always", inline: "systemctl restart pomegranate.service"

	config.vm.provider "virtualbox" do |v|
		v.memory = $MEMORY
		v.cpus = $CPUS
	end
end
