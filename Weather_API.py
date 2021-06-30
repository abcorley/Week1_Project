import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

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
"""Creating a dictionary to load data from API"""

Weather_dict = {}
i = 1

for weather in data['days']:
    Weather_dict[i] = [weather['datetime'], weather['temp']]
    i += 1
"""Converting Dict to DataFrame"""

weather_df = pd.DataFrame.from_dict(Weather_dict,
                                    orient='index', columns=['Date', 'Temp'])

engine = create_engine('mysql://root:codio@localhost/Weather')

weather_df.to_sql(Location, con=engine, if_exists='replace', index=False)
