#! /usr/bin/env bash

echo "Hasdev dependencies installer."
echo "Updating software repo lists..."
echo ""
sudo apt-get update

echo ""
echo "Installing basic tools..."
echo ""
sudo apt-get install -y python-dev gcc g++ binutils build-essential git make curl wget

echo ""
echo "Installing other libraries, used as extensions by various Hasgeek apps..."
echo ""
sudo apt-get install -y libxml2 libxml2-dev libxslt1-dev libffi-dev

echo ""
echo "Installing Postfix."
sudo apt-get install postfix
echo "Postfix is now installed. Please don't forget to configure your SMTP settings in /etc/postfix/main.cf"

echo ""
echo "Installing PostgreSQL."
sudo apt-get install postgresql libpq-dev

echo ""
echo "Installing Redis."
sudo apt-get install redis-server

echo ""
echo "Installing Chris Lea's PPA for the latest versions of Node.js, used as a JS runtime..."
sudo apt-get install -y python-software-properties software-properties-common
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install -y nodejs
echo ""

echo "All dependencies have been installed. Feel free to submit a PR with any additional packages, as and when needed." 

