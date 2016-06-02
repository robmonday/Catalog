#Linux Server Configuration 

This assigned project is part of the Udacity Fullstack Nanodegree.  The Catalog project (formerly project 3) has be loaded onto the configured Linux server in order to demonstrate end-to-end capability.

##Project Overview

Take a baseline installation of a Linux distribution on a virtual machine and prepare it to host web applications, including installing updates, securing from a number of attack vectors and installing/configuring web and database servers.

This assignement teaches how to access, secure, and perform the initial configuration of a bare-bones Linux server. It also requires the studen to demonstrate knowledge about how to install and configure a web and database server and actually host a web application.

##Required Components

IP address: <a href="http://52.37.6.235" target="_blank">52.37.6.235</a><br>
SSH port: 2200<br>
Public URL: <a href="http://ec2-52-37-6-235.us-west-2.compute.amazonaws.com" target="_blank">http://ec2-52-37-6-235.us-west-2.compute.amazonaws.com</a><br>

##Summary of Software Installed and Configuration Changes Made

1. Created VM with Udacity account, move private key into .ssh folder, set private key permissions to read/write for owner only, SSH into server (`mv ~/Downloads/udacity_key.rsa ~/.ssh`, `chmod 600 ~/.ssh/udacity_key.rsa`, `ssh -i ~/ssh/udacity_key.rsa root@52.37.6.235`)

1. Created new user named grader (`sudo adduser grader`) and gave permission to sudo (`visudo`, added `grader ALL=(ALL:ALL) ALL` code using editor)

1. Updated and upgraded the latest software packages (`apt-get update`, `apt-get upgrade`)

1. Changed the SSH port from 22 to 2200, prevent login as root, allow password authentication, give grader access to login, access server using grader user (`nano /etc/ssh/sshd_config`, changed port to 2200 in code number using editor, `PermitRootLogin without-password`, `PasswordAuthentication yes`, added to end `UseDNS no` & `AllowUsers grader`, `service ssh restart`, `exit`, `ssh grader@52.37.6.235 -p 2200`)


1. Configured Uncomplicated Firewall (UFW) to only allow specified incoming connections (`sudo ufw status`, `sudo ufw default deny incoming`, `sudo ufw default allow outgoing`, `sudo ufw allow ssh`, `sudo ufw allow 2200`, `sudo ufw allow 80`, `sudo ufw allow 123`, `sudo ufw status` to check results, `sudo ufw enable`)

1. Configured the local timezone to UTC (`sudo dpkg-reconfigure tzdata`, selected etc > /UTC using menu, `sudo apt-get install ntp`)

1. Installed and configured Apache to serve a Python mod_wsgi application (`sudo apt-get install apache2`, check IP address to be sure 'it works' page is displaying, `sudo apt-get install python-setuptools`, `sudo apt-get install libapache2-mod-wsgi`)

1. Installed Git (`sudo apt-get install git`, `git config --global user.name 'Rob Monday'`, `git config --global user.email 'rob.monday@gmail.com'`)

1. Installed Flask and all necessary pre-requisites (`sudo apt-get install libapache2-mod-wsgi`, `sudo apt-get install python-dev`, `sudo a2enmod wsgi`, `sudo apt-get install python-pip`, `sudo pip install virtualenv`, `sudo virtualenv venv`, set completely open permissions for virtual environment `sudo chmod -R 777 venv`, activate virtual environment `source venv/bin/activate`, `sudo apt-get install python-setuptools`, `sudo pip install Flask`, `sudo pip install httplib2`, `sudo pip install requests`, `sudo pip install flask-seasurf`, `sudo apt-get install python-psycopg2`, `sudo pip install oauth2client`, `sudo pip install sqlalchemy`, lastly `deactivate` venv)

1. Move Udacity Project 3 to Linux server and link files appropriately (On local machine: rename `server.py` from Udacity project 3 to `__init__.py`, create new git repo `git init`, `git remote add origin https://github.com/robmonday/Catalog.git`, `git add *`, `git commit -m 'initial commit'`, `git push origin master`)  Then (on Linux server:  `cd /var/www/`, `git clone https://github.com/robmonday/Catalog.git`, `sudo nano .htaccess` and paste in `RedirectMatch 404 /\.git`)

1. Create and enable host configuration (`sudo nano /etc/apache2/sites-available/catalog.conf`, type in code, `sudo a2ensite catalog.wsgi`, create `catalog.wsgi` in Catalog folder with appropriate import from `__init__.py`, `sudo service apache2 restart`)

1.  Reconfigured database to work with PostgreSQL rather than SQLite (`sudo apt-get install postgresql postgresql-contrib`, `/var/www/Catalog/catalog$ sudo nano database_setup.py` then replace 'sqlite:///apartment-inventory.db'` with `'postgresql://catalog:robspassword@localhost/catalog'`)

1. Installed PostgreSQL, then created created and configured `catalog` user (`apt-get install postgresql postgresql-contrib`, `/etc/init.d/postgresql start`, `??`)

1.  Imported former project 3 'Catalog' app, updated OAuth2, and linked separate files as appropriate (``)


##List of Other 3rd-Party Resources
- www.stackoverflow.com
- https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
- http://www.2daygeek.com/how-to-change-the-ssh-port-number/#
- http://askubuntu.com/questions/138423/how-do-i-change-my-timezone-to-utc-gmt
- http://stackoverflow.com/questions/28253681/you-need-to-install-postgresql-server-dev-x-y-for-building-a-server-side-extensi
- www.sqlalchemy.org
- http://flask.pocoo.org


##Other Helpful Links
<a href="https://www.udacity.com/account#!/development_environment" target="_blank">Link to Development Environment</a>
<br>
<a href="https://docs.google.com/document/d/1J0gpbuSlcFa2IQScrTIqI6o3dice-9T7v8EDNjJDfUI/pub?embedded=true" target="_blank">Getting Started Guide</a>
