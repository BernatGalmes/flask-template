from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
api = Api()
# Initialize Marshmallow
ma = Marshmallow()
