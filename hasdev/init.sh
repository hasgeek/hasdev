#! /usr/bin/env bash

function hr(){
	echo ""
	echo "====================================="
	echo ""
}

hr
echo "Running Ubuntu update..."
hr
apt-get update
hr
echo "Installing make..."
hr
apt-get install -y make -qq
hr
echo "Installing curl..."
hr
apt-get install -y curl -qq
hr
echo "Installing unzip..."
hr
apt-get install -y unzip -qq
hr
echo "Installing python-dev..."
hr
apt-get install -y python-dev -qq
hr
echo "Installing libjpeg-dev..."
hr
apt-get install -y libjpeg-dev -qq
hr
echo "Installing libpng-dev..."
hr
apt-get install -y libpng-dev -qq
hr
echo "Installing libfreetype6-dev..."
hr
apt-get install -y libfreetype6-dev -qq
hr
echo "Installing libwebp-dev..."
hr
apt-get install -y libwebp-dev -qq
hr
echo "Installing liblcms1-dev..."
hr
apt-get install -y liblcms1-dev -qq
hr
echo "Installing python setuptools ..."
hr
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
python ez_setup.py
rm ez_setup.py
rm setuptools-*
hr
echo "Installing python pip ..."
hr
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
rm get-pip.py
hr
echo "Installing postgress..."
hr
apt-get install -y postgresql postgresql-contrib python-psycopg2 libpq-dev build-essential
hr
echo "Setting up postgres..."
hr
sudo -u postgres createuser -SDRl hasgeek
sudo -u postgres psql -c "ALTER USER hasgeek WITH PASSWORD 'hasgeek'"
hr
echo "Installing redis-server..."
hr
apt-get install -y redis-server -qq
hr
echo "Installing openjdk-7-jre-headless..."
hr
apt-get install -y openjdk-7-jre-headless -qq
hr
echo "Installing nodejs..."
hr
apt-get install -y nodejs -qq
hr
# https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#ubuntu-mint-elementary-os
# Please report any errors you may face with nodejs on the Issue Tracker for hasweb
echo "Installing npm..."
hr
apt-get install -y npm -qq
hr
echo "Installing compass..."
hr
gem install compass
hr

echo "Updating /etc/hosts file on virtual machine..."
python /vagrant/hasdev/hosts.py

# echo "Installing uglifyjs..."
# npm install uglify-js
# uglifyjs installs are just failing because of some dependency on nodejs app source-map.
# hr