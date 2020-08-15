#
# Pulling data from WUnderground and sending to Wavefront by Python
#
# Core original code written by Durren Shen @durrenshen 
# in a blog at https://www.wavefront.com/weather-metrics/
# 
# Cleaned up by Bill Roth @BillRothVMware
#
import urllib2
import json
import logging
import socket
import sys
import time
import re
import syslog

#
# Below assumes the proxy is running on the same system. YMMV
#
# Get epoch time 
#
epochtime = time.time()
#
# Add your key here. You can get an API key here: https://www.wunderground.com/weather/api/
# Also change KCASANJO821.json to your station. Or you can use this one.
# 
try:
  f = urllib2.urlopen('https://api.ambientweather.net/v1/devices/EC:FA:BC:07:F2:09?apiKey=89bdfb21c96743ea9781ee700f71c6ae9b1856371f164e6aa3384c8995f1bcdc&applicationKey=63bbc94527b54b66b2e588d89d9c71c9aedb36a1f5e643459c12f691573678a0&limit=1')
except urllib2.HTTPError, e:
  print('HTTPError = ' + str(e.code))
  quit(-1)

json_string = f.read()
parsed_json = json.loads(json_string)

observation_epoch = parsed_json[0]['dateutc']
sepochtime=str(observation_epoch / 1000)
print('weather.observationEpoch.cottle ' +  sepochtime + ' ' + str(int(epochtime)))

temp_f = parsed_json[0]['tempf']
print('weather.temp_f.cottle ' + str(temp_f) + ' ' + sepochtime)

tempin_f = parsed_json[0]['tempinf']
print('weather.temp_f.inside.cottle ' + str(tempin_f) + ' ' + sepochtime)

humidity = parsed_json[0]['humidity']
print('weather.humidity.cottle ' + re.sub("[^0-9]", "", str((humidity))) + ' ' + sepochtime)  

wind_degrees = parsed_json[0]['winddir']
print('weather.wind_degrees.cottle ' + str(wind_degrees) + ' ' + sepochtime)

wind_mph = parsed_json[0]['windspeedmph']
print('weather.wind_mph.cottle ' + str(wind_mph) + ' ' + sepochtime)

wind_gust_mph = parsed_json[0]['windgustmph']
print('weather.wind_gust_mph.cottle ' + str(wind_gust_mph) + ' ' + sepochtime)

pressure_in = parsed_json[0]['baromabsin']
print('weather.pressure_in.cottle ' + str(pressure_in) + ' ' + sepochtime)

dewpoint_f = parsed_json[0]['dewPoint']
print('weather.dewpoint_f.cottle ' + str(dewpoint_f) + ' ' + sepochtime)

solarradiation = parsed_json[0]['solarradiation']
print('weather.solarradiation.cottle ' + str(solarradiation) + ' ' + sepochtime)

UV = parsed_json[0]['uv']
print('weather.UV.cottle ' + str(UV) + ' ' + sepochtime)

precipRt = parsed_json[0]['hourlyrainin']
print('weather.precipRate.cottle ' + str(precipRt) + ' ' + sepochtime)

precipDaily = parsed_json[0]['dailyrainin']
print('weather.precipRate.cottle.daily ' + str(precipDaily) + ' ' + sepochtime)

precipMonthly = parsed_json[0]['monthlyrainin']
print('weather.precipRate.cottle.monthly ' + str(precipMonthly) + ' ' + sepochtime)


precip_total = parsed_json[0]['totalrainin']
print('weather.precipRate.cottle.yearly ' + str(precip_total) +' ' + sepochtime)

syslog.syslog('Weather logged at ' + str(observation_epoch));
f.close();
