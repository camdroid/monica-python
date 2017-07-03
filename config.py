import configparser

config = configparser.ConfigParser()

config.read('databases.toml')
try:
    default = config.get('default', {})
except:
    default = {}

db_host = default.get('host', '127.0.0.1')
db_pass = default.get('pass', '')
db_user = default.get('user', 'ubuntu')
db_name = default.get('name', 'circle-test')
