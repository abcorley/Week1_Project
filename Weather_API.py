import requests
import json

BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices'

BASE_URL2 = '/rest/services/timeline/'

API_Key = 'LCRCQE8SWKLGXT6837WYWGATZ'

Location = input('Enter a city: ')

response = requests.get(BASE_URL + BASE_URL2 + Location + '?key=' + API_Key)
data = response.json()

"""Days key includes daily info:
      datetime: yyyy-mm-dd
      temp,
      feelslike,
      precipitation,
      etc.
"""

for weather in data['days']:
    print(weather['datetime'], weather['temp'])
