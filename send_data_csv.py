#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading
from datetime import datetime

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      print 'next'
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the $

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    initial_time = datetime.now()
    buffer = []
    old_buffer_value = ""
    while True:
      current_time = datetime.now()
      time_diff = current_time - initial_time
      if (int(time_diff.total_seconds()) % 10 == 0):
        # Every 10 seconds add buffer contents to list
        buffer.append('lat: ' + str(gpsd.fix.latitude) + ', long: ' + str(gpsd.fix.longitude) + ', time utc: '
                      + str(gpsd.utc) + ', speed (m/s): ' + str(gpsd.fix.speed))

      else:
          if old_buffer_value == buffer[-1]: # If old buffer = new buffer do nothing
              pass
          elif old_buffer_value != buffer[-1]: # else update buffer and print new value
              print(buffer[-1])
              old_buffer_value = buffer[-1]

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."