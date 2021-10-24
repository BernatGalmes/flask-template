import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '../..')

load_dotenv(str(APP_ROOT) + os.path.sep + '.env')  # reading .env.example file

secret_key = os.getenv('APP_SECRET_KEY')
PWD = os.path.abspath(os.curdir)

DEBUG = os.getenv('APP_DEBUG', default=False)

SQLALCHEMY_DATABASE_URI = os.getenv('APP_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('APP_DATABASE_TRACK_MODIFICATIONS', default=False)

