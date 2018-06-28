#!/bin/bash
echo "Initialising GPSD"
sudo killall gpsd
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
echo "Done! Deploy your application"
