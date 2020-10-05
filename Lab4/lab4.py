import urllib.request
import requests

URL = 'https://api.thingspeak.com/update?api_key='

KEY = '54CDA6FJF4RCJ92C'

HEADER = '&field1={}&field2={}&field3={}'.format("millertimlin@cmail.carleton.ca", "L2-M-6", "a")

NEW_URL = URL+KEY+HEADER

data=urllib.request.urlopen(NEW_URL)
