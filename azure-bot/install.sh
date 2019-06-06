#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

cp lanyard-bot.service /lib/systemd/system/

mkdir -p /opt/lanyard
cp env.sh /opt/lanyard
cp bot.py /opt/lanyard

pip3 install -r requirements.txt

systemctl enable lanyard-bot.service
systemctl start lanyard-bot.service

