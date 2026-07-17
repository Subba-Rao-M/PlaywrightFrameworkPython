import configparser
import os

import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    # Build an absolute path to properties.ini based on THIS file's location,
    # so it works regardless of the current working directory.
    properties_path = os.path.join(os.path.dirname(__file__), 'properties.ini')
    files_read = config.read(properties_path)  # read the properties file and store the data in config variable
    # configparser silently ignores a missing file, so verify it was actually loaded.
    if not files_read:
        raise FileNotFoundError(f"Could not find configuration file: {properties_path}")
    return config


def getPassword():
    return "Password"

connect_config = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' :getConfig()['SQL']['database'],
}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config) # ** indicates dictionary values are passed
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


# To get the row from db based on query passed
def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row