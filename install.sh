#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

cp lanyard/lanyard.service /lib/systemd/system/
cp twilio/twilio-listener.service /lib/systemd/system/

mkdir -p /opt/lanyard
cp azure-bot/env.sh /opt/lanyard
cp lanyard/lanyard-controller.py /opt/lanyard
cp twilio/twilio-listener.py /opt/lanyard
cp -r lanyard/effects/ /opt/lanyard
touch /tmp/messages.queue

systemctl enable lanyard.service
systemctl start lanyard.service
systemctl enable twilio-listener.service
systemctl start twilio-listener.service
