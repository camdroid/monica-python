import configparser

config = configparser.ConfigParser()

config.read('database.toml')

options = config['default']

db_host = options['db_host']
db_name = options['db_name']
db_user = options['db_user']
db_pass = options['db_pass']

