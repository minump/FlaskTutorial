from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    # @app.route("/footer", methods=["GET"])
    # def index():
    return 'Hello World'

#@app.route("/footer", methods=["GET"])
#def index():
