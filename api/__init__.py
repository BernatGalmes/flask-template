from flask import Flask
from api import settings
from api.extensions import db, ma, api


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    from api.routes import register_routes
    register_routes(app, api)

    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)



