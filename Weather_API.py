import os
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import sqlalchemy
from sqlalchemy import create_engine


"""Contributors: Nikhil Yadav"""

global api_key
api_key = 'LCRCQE8SWKLGXT6837WYWGATZ'

"""Determines if User wants to overwrite or update the database"""


def menu_filesinput():
    print('Do you have a file you want to load?')
    return input('Enter 1 if yes and 0 if no: ')


def menu_changesinput():
    print('1). Overwrite the database')
    print('2). Update the database')
    print('3). Just load the database')
    return input('Enter Option: ')


"""Creates a database"""


def create_database(database_name):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + database_name+';"')


"""Saves the database to a file"""


def save_database(database_name, sql_filename):
    os.system('mysqldump -u root -pcodio ' + database_name + '>'
              + sql_filename)


"""Loads a file into a database"""


def load_database(database_name, sql_filename):
    os.system("mysql -u root -pcodio "+database_name+" < " + sql_filename)


def loadNewData(dataframe, table_name):
    dataframe.sort_values(by='Date', inplace=True, ascending=False)
    date_object = datetime.strptime(dataframe.iloc[0, 0], '%Y-%m-%d')
    date_object = date_object + timedelta(days=1)
    recent_date = date_object.strftime("%Y-%m-%d")
    mostRecent = get_data('https://weather.visualcrossing.com/'
                          + 'VisualCrossingWebServices/rest/services/timeline/'
                          + table_name + '/' + recent_date + '/?key='
                          + api_key)
    update_Dict = create_Dict(mostRecent)
    return dict_to_dataframes(update_Dict)


def loadDataset(database_name, table_name, filename, update=False):
    load_database(database_name, filename)
    engine = create_engine('mysql://root:codio@localhost/' + database_name)
    df = pd.read_sql_table(table_name, con=engine)
    if update:
        return loadNewData(df, table_name)
    else:
        return df


def get_info():
    location = input('Enter a city: ')
    database_name = input('Enter the name of the database: ')
    return location, database_name


def get_file_info():
    database_name = input('Enter the name of the database: ')
    filename = input('Enter the name of the file: ')
    table_name = input('Enter the name of the table: ')
    return database_name, filename, table_name


def create_URL(location):
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


def create_Table(dataFrame, location, changes='replace'):
    engine = create_engine('mysql://root:codio@localhost/Weather')
    dataFrame.to_sql(location, con=engine, if_exists=changes, index=False)


"""Main"""
if __name__ == "__main__":
    file_response = menu_filesinput()
    if file_response == '1':
        database_name, filename, table_name = get_file_info()
        changes_response = menu_changesinput()
        if changes_response == '2':
            dataframe = loadDataset(database_name, table_name, filename,
                                    update=True)
            create_Table(dataframe, table_name, changes='append')
        elif changes_response == '1':
            create_database(database_name)
            url = create_URL(table_name)
            response = get_data(url)
            new_dict = create_Dict(response)
            dataframe = dict_to_dataframes(new_dict)
            create_Table(dataframe, table_name)
        else:
            load_database(database_name, filename)
    else:
        location, database_name = get_info()
        create_database(database_name)
        url = create_URL(location)
        response = get_data(url)
        new_dict = create_Dict(response)
        dataframe = dict_to_dataframes(new_dict)
        create_Table(dataframe, location)
    save_database(database_name, filename)
