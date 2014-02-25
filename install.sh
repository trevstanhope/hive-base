#!/bin/bash
wget -q -O http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
apt-get update
apt-get upgrade
apt-get install pip virtualenv curl jenkins
pip install -r requirements.txt
cp apache/* /etc/apache2/sites-available/
a2enmod proxy
a2ensite jenkins
<<<<<<< HEAD
a2ensite flask
=======
>>>>>>> e833faead1c0ceea92c91566a7cf41a72b5b37b0
a2dissite default

