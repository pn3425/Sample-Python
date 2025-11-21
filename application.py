from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Hello from NEW Python App!\nCI/CD pipeline working"
