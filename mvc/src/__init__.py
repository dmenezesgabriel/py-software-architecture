import logging
import os

from dotenv import load_dotenv  # Import load_dotenv
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)

    # Configure the logging level to DEBUG
    app.logger.setLevel(logging.DEBUG)

    # Create a console handler and set the level to DEBUG
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    # Add the handler to the app's logger
    app.logger.addHandler(ch)

    # Configure the application
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the database
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    # Register routes
    from src.controllers import register_routes

    register_routes(app)

    @app.route("/hello")
    def hello_world():
        return jsonify({"message": "Hello, World!"})

    return app
