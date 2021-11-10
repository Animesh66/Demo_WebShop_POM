from configparser import ConfigParser


def configuration_reader(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\conf.ini")
    return config.get(section, key)



