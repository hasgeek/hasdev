#! /usr/bin/env bash

mkdir logs

echo "Running Ubuntu update..."
apt-get update > logs/apt-get-update.log

echo "Installing curl..."
apt-get install -y curl > /vagrant/logs/apt-get-install.log
echo "Installing python-dev..."
apt-get install -y python-dev >> /vagrant/logs/apt-get-install.log
echo "Installing redis-server..."
apt-get install -y redis-server >> /vagrant/logs/apt-get-install.log
echo "Installing nodejs..."
apt-get install -y nodejs >> /vagrant/logs/apt-get-install.log
# https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#ubuntu-mint-elementary-os
# Please report any errors you may face with nodejs on the Issue Tracker for hasweb
echo "Installing openjdk-7-jre..."
apt-get install -y openjdk-7-jre >> /vagrant/logs/apt-get-install.log
echo "Installing make..."
apt-get install -y make >> /vagrant/logs/apt-get-install.log
echo "Installing unzip..."
apt-get install -y unzip >> /vagrant/logs/apt-get-install.log
echo "Installing npm..."
apt-get install -y npm >> /vagrant/logs/apt-get-install.log

echo "Installing python distribute ..."
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py > /vagrant/logs/python-setups.log
rm distribute_setup.py

echo "Installing python pip ..."
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py >> /vagrant/logs/python-setups.log
rm get-pip.py

echo "Installing compass..."
gem install compass > /vagrant/logs/compass-install.log

echo "Installing uglifyjs..."
npm install uglifyjs > /vagrant/logs/uglifyjs-install.log