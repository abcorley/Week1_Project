import os
import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

def menu_input():
    print('1). Have Weather.sql')
    print('2). Do not have Weather.sql')
    return input('Enter Option:')


def create_database():
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS Weather;"')


def save_database():
    os.system("mysqldump -u root -pcodio Weather > Weather.sql")


def load_database():
    os.system("mysql -u root -pcodio Weather < Weather.sql")
  
  
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
    return response


"""Days key includes daily info:
      datetime: yyyy-mm-dd
      temp,
      feelslike,
      precipitation,
      etc.
"""
"""Creating a dictionary to load data from API"""


def create_Dict(response):
    data = response.json()
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


"""Main"""
if __name__ == "__main__":
    option = menu_input()
    if option == 1:
        load_database()
    else:
        create_database()
    change_option = changes_menu()
    key, location = get_info()
    while len(key) != 25:
        key = input('Enter API Key:')
    while location == '':
        location = input('Enter a city: ')
    url = create_URL(key, location)
    response = get_data(url)
    if response.status_code == 200:
        dictionary = create_Dict(response)
        df = dict_to_dataframes(dictionary)
        create_Table(df, location)
    else:
        print('Could not access data')
    save_database()
