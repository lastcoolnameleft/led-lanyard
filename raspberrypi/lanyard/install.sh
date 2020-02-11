#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

cp lanyard.service /lib/systemd/system/

mkdir -p /opt/lanyard
cp env.sh /opt/lanyard
cp lanyard-controller.py /opt/lanyard
cp -r effects/ /opt/lanyard
pip3 install -r requirements.txt
touch /tmp/messages.queue

systemctl enable lanyard.service
systemctl restart lanyard.service