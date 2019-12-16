from flask import Flask
from utils.api import api_response, api_res_type

import json

with open("stubs/products.json") as products_stub:
    products_json = products_stub.read()

products = json.loads(products_json)

app = Flask(__name__)

@app.route("/api/")
def hello():
    return api_response(
        api_res_type["success"],
        products,
    )
