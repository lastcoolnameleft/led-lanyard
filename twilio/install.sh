#!/usr/bin/env bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit 1
fi

cp twilio-listener.service /lib/systemd/system/

cp twilio-listener.py /opt/lanyard

systemctl enable twilio-listener.service
systemctl start twilio-listener.service
