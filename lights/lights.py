#!/usr/bin/python
#origional on-off script obtained from https://www.raspberrypi.org/forums/viewtopic.php?t=152742
#and modified to adjust to sunrise/sunset with https://github.com/SatAgro/suntime

import time, datetime
from random import randint
from suntime import Sun, SunTimeException
from datetime import timedelta, datetime

#our location.  you can look this up with Google maps
latitude = 33.01
longitude = -96.60
sun = Sun(latitude,longitude)

#import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)   #Use BCM GPIO numbers

#Define GPIO mapping
Relay_ON = 19

#GPIO.setup(Relay_ON, GPIO.OUT)   #Relay enable
#GPIO.output(Relay_ON, GPIO.LOW)  # default set low
time.sleep(1)                    # delay to prevent relay switching to fast

#Get sunrise and sunrise
today_sr = sun.get_local_sunrise_time()
today_ss = sun.get_local_sunset_time()

stuff = today_sr.split()

#define relay off and on time based on sunset and sunrise
R1OFFH = int(today_sr.strftime('%H'))
R1OFFM = int(today_sr.strftime('%M'))

R1ONH = int(today_ss.strftime('%H'))
R1ONM = int(today_ss.strftime('%M'))

#Define relay on times
#R1ONH = 13
#R1ONM = randint(5, 15)
#R1ONS = 0

#Define relay off times
#R1OFFH = 6
#R1OFFM = randint(5, 15)
#R1OFFS = 0

# test for relay current state
dt = list(time.localtime())
hour = dt[3]
minute = dt[4]
second = dt[5]
print(hour,minute, second)

# check for right hour and mins , seconds equal or greater than on time
if hour == R1ONH:
  if minute >= R1ONM:
#    if second >= R1ONS:
      print("on")
      #GPIO.output(Relay_ON, GPIO.HIGH)

# check for hours greater than on time but less than off time
if hour > R1ONH or hour < R1OFFH:
  print("greater on")
  #GPIO.output(Relay_ON, GPIO.HIGH)

# check for correct off hours but mins seconds less than off time
if hour == R1OFFH:
  if minute < R1OFFM:
#    if second < R1OFFS:
      print("less off")
      #GPIO.output(Relay_ON, GPIO.HIGH)



while True:
  dt = list(time.localtime())
  hour = dt[3]
  minute = dt[4]
  second = dt[5]
  time.sleep(1)
  print(hour,minute,second)


  if hour == R1ONH:
    if minute == R1ONM:
#      if second == R1ONS:
        print("loop on")
        #GPIO.output(Relay_ON, GPIO.HIGH)

  if hour == R1OFFH:
    if minute == R1OFFM:
#      if second == R1OFFS:
        print("loop off")
        #GPIO.output(Relay_ON, GPIO.LOW)

        #after we turn off update sunrise and sunset
        today_sr = sun.get_local_sunrise_time()
        today_ss = sun.get_local_sunset_time()

        #define relay off and on time based on sunset
        R10FFH = int(today_sr.strftfime('%H'))
        R10FFM = int(today_sr.strftime('%M'))

        R10NH = int(today_ss.strftime('%H'))
        R10NM = int(today_ss.strftime('%M'))
