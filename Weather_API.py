import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

def get_info():
    api_key = input('Enter API Key:')
    location = input('Enter a city: ')
    return api_key, location
  
def create_URL(api_key, location):
    BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices'
    BASE_URL2 = '/rest/services/timeline/'
    return BASE_URL + BASE_URL2 + location + '?key=' + api_key
  
def get_data(URL):
    response = requests.get(URL)
    return response.json()

"""Days key includes daily info:
      datetime: yyyy-mm-dd
      temp,
      feelslike,
      precipitation,
      etc.
"""
"""Creating a dictionary to load data from API"""

def create_Dict(data):
    Weather_dict = {}
    i = 1
    for weather in data['days']:
        Weather_dict[i] = [weather['datetime'], weather['temp']]
        i += 1
    return Weather_dict
  
"""Converting Dict to DataFrame"""

def dict_to_dataframes(dictionary):
    return pd.DataFrame.from_dict(dictionary,
                                  orient='index', columns=['Date', 'Temp'])
    
def create_Table(dataFrame, location):
    engine = create_engine('mysql://root:codio@localhost/Weather')
    dataFrame.to_sql(location, con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    key, location = get_info()
    url = create_URL(key,location)
    data = get_data(url)
    dictionary = create_Dict(data)
    df = dict_to_dataframes(dictionary)
    create_Table(df, location)