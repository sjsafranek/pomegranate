# -*- mode: ruby -*-
# vi: set ft=ruby :

# DeoDjango Vagrant Box
# https://github.com/david-wilson/vagrant-geodjango-base

# VM Customized Settings
$CPUS              = 1
$MEMORY            = 512

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

#Vagrant::Config.run do |config|
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	# Base box to build off, and download URL for when it doesn't exist on the user's system already
	#config.vm.box = "ubuntu/trusty32"
	config.vm.box = "debian/jessie64"
	#config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"

	# As an alternative to precise32, VMs can be built from the 'django-base' box as defined at
	# https://github.com/torchbox/vagrant-django-base , which has more of the necessary server config
	# baked in and thus takes less time to initialise. To go down this route, you will need to build
	# and host django-base.box yourself, and substitute your own URL below.
	#config.vm.box = "django-base-v2.2"
	#config.vm.box_url = "http://vmimages.torchbox.com/django-base-v2.2.box"  # Torchbox-internal URL to django-base.box
	
	# Boot with a GUI so you can see the screen. (Default is headless)
	# config.vm.boot_mode = :gui
	
	# Assign this VM to a host only network IP, allowing you to access it
	# via the IP.
	# config.vm.network "33.33.33.10"
	
	# Forward a port from the guest to the host, which allows for outside
	# computers to access the VM, whereas host only networking does not.
	config.vm.network :forwarded_port, guest: 8080, host: 8080
	#config.vm.network "private_network", ip: "172.20.0.10", netmask: "255.240.0.0", :mac => "08002719318B"
	
	# Share an additional folder to the guest VM. The first argument is
	# an identifier, the second is the path on the guest to mount the
	# folder, and the third is the path on the host to the actual folder.
	#config.vm.share_folder "project", "/home/vagrant/{{ project_name }}", "."
	
	# Enable provisioning with a shell script.
	#config.vm.provision :shell, :path => "etc/install/install.sh", :args => "{{ project_name }}"
	#config.vm.provision "shell", inline: 'aptitude -yy upgrade turnstile'
	#sudo apt-get install python3-pip
	#  sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
	config.vm.provision "shell", inline: 'aptitude update'
	config.vm.provision "shell", inline: 'aptitude -yy install install libgeos++'
	config.vm.provision "shell", inline: 'aptitude -yy install install binutils libproj-dev gdal-bin'
	config.vm.provision "shell", inline: 'aptitude -yy install python3-pip'
	config.vm.provision "shell", inline: 'aptitude -yy install python3-gdal'
	#config.vm.provision "shell", inline: 'aptitude -yy install python3-django'
	config.vm.provision "shell", inline: 'pip3 install django'
	config.vm.provision "shell", inline: 'aptitude -yy install python3-jinja2'
	config.vm.provision "shell", inline: 'cd /vagrant; python3 manage.py runserver 0.0.0.0:8080 &'

	config.vm.provider "virtualbox" do |v|
		v.memory = $MEMORY
		v.cpus = $CPUS
	end
end
