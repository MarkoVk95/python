from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    with open('/python/json/test.json') as f:
        data = json.load(f)
    return data
