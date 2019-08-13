from dotenv import load_dotenv
from os.path import join, dirname
from os import getenv

env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)

# Mysql database
MYSQL_DATABASE = getenv('MYSQL_DATABASE')
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_HOST = getenv('MYSQL_HOST')
MYSQL_PASSWORD = getenv('MYSQL_PASSWORD')

# Discord bot token
DISCORD_TOKEN = getenv('DISCORD_TOKEN')
