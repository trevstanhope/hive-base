#!/bin/bash
wget -q -O http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
apt-get update
apt-get upgrade
apt-get install pip virtualenv curl
pip install -r requirements.txt



