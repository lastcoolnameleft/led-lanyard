#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

cp twilio-listener.service /lib/systemd/system/

mkdir -p /opt/lanyard
cp twilio-listener.py /opt/lanyard
cp -r templates /opt/lanyard
pip3 install -r requirements.txt

systemctl enable twilio-listener.service
systemctl restart twilio-listener.service
