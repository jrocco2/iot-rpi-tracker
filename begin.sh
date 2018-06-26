#!/bin/bash
echo "GPS Initialising"
sudo killall gpsd
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock

echo "Activate Python Script"
python testgps1.py