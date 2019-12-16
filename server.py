from flask import Flask
from utils.api import api_response, api_res_type

import json

with open("stubs/products.json") as myfile:
    data = myfile.read()

obj = json.loads(data)

app = Flask(__name__)

@app.route("/api/")
def hello():
    return api_response(
        api_res_type["success"],
        obj,
    )

@app.route("/api/smth", methods=["GET"])
def getSmth():
    return api_response(
        api_res_type["success"],
    )
