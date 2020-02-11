#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

# Used for static bot framework page
sudo apt-get -y install build-essential libssl-dev libffi-dev python-dev lighttpd

cp index.html /var/www/html/index.html

cp azure-bot.service /lib/systemd/system/

mkdir -p /opt/lanyard
cp bot.py /opt/lanyard
cp ngrok.yaml /opt/ngrok

pip3 install -r requirements.txt

systemctl enable azure-bot.service
systemctl restart azure-bot.service
