from flask import Flask
from Controllers.store_controller import store_controller

app = Flask(__name__)

app.register_blueprint(store_controller)

