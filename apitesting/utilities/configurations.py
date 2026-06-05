import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')  # read the properties file and store the data in config variable\
    return config


def getPassword():
    return "Password"