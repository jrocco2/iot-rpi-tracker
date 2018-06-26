#!/bin/bash
echo "Downloading Required Files"
sudo apt-get install dos2unix
sudo apt-get install gpsd gpsd-clients python-gps

echo "GPS Initialising"
sudo killall gpsd
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock

echo "Activate Python Script"
dos2unix send_data.py
python send_data.py