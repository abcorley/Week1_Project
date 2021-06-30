import requests
import json

BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices'

BASE_URL2 = '/rest/services/timeline/'

API_Key = 'LCRCQE8SWKLGXT6837WYWGATZ'

Location = 'New York City'

Date1 = '2020-07-01'

Date2 = '2020-07-02'

"""for 15 day forcatse instead of Date1 and Date2 use timeline"""

response = requests.get(BASE_URL + Base_URL2 +  Location + '/' + Date1 + '/' + Date2 + '?key=' + API_Key)
data = response.json()

for key, value in data.items():
    print(key, ':', value)

"""Days key includes daily info:
      datetime: yyyy-mm-dd
      temp,
      feelslike,
      precipitation,
      etc.
"""

for weather in data['days']:
   print(weather['datetime'], weather['temp'])
