import configparser, pathlib

ini_path = pathlib.Path(__file__).parents[1] / "data/budget.ini"

def _config_get():
    #! log it
    config = configparser.ConfigParser()
    config.read(ini_path)
    return config

def _config_write(config):
    #! log it
    with open(ini_path, "w") as open_ini:
        config.write(open_ini)

def value_get(ini_heading, header_value):
    #! log it
    return _config_get()[ini_heading][header_value]

def value_set(ini_header, header_value, value):
    #! log it
    config = _config_get()
    config[ini_header][header_value] = value
    _config_write(config)

"""
added the lock get function rather than accessing the value with the existing method
because of the convinience that this function brings when dealing with values that are
not as clean as they should be // the bool() function returns True as soon the str is
not empty or states "False" case insensitive, the function also deals with missing values
"""
def lock_get():
    #!log it
    return _config_get().getboolean("CONTROL", "lock")
    