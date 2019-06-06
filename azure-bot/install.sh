#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

# Used for static bot framework page
apt-get install lighttpd
cp index.html /var/www/html/index.html

cp lanyard-bot.service /lib/systemd/system/

mkdir -p /opt/lanyard
cp env.sh /opt/lanyard
cp bot.py /opt/lanyard
cp ngrok.yaml /opt/ngrok

pip3 install -r requirements.txt

systemctl enable lanyard-bot.service
systemctl restart lanyard-bot.service
