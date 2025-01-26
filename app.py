from Utils.config import DevConfig
from flask import Flask
from Blueprints.products import products
from Blueprints.authentication import authentication
from Models.models import db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


def create_app(config_class=DevConfig):
    """
    Creates app with given config class
    :param config_class:
    :return: flask app object
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    app.register_blueprint(products, url_prefix="/product")
    app.register_blueprint(authentication, url_prefix="/user")

    # Boot up app Models.
    extensions(app)

    # Register models
    # with app.app_context():
    #     db.create_all()
    return app


def extensions(current_app):
    """
    Register 0 or more Models (mutates the app passed in).
    :param current_app: Flask application instance
    :return: None
    """
    db.init_app(current_app)


app = create_app()
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


def __repr__(self) -> str:
    return f"{self.sno}-{self.Name}-{self.Price}"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
