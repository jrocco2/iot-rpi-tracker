#! /usr/bin/python
from gps import *
from datetime import datetime

if __name__ == '__main__':
  gpsd = gps(mode=WATCH_ENABLE)
  try:
    initial_time = datetime.now()
    buffer = []
    old_buffer_value = ""
    while True:
      gpsd.next()
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
    print "\nGoodbye"