from flask import Flask
from app.home import bl_home


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    app.register_blueprint(bl_home)

    return app
