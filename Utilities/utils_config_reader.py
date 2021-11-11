from configparser import ConfigParser


def configuration_reader(section, key):
    config = ConfigParser()
    config.read(".\\Configuration_Data\\config.ini")
    return config.get(section, key)


