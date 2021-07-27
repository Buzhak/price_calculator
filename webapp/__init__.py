from flask import Flask

from webapp.calculator.routes import calculator_bp

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(calculator_bp)

    return app