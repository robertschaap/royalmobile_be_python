from controllers.products import products_controller, get_products
from flask import Flask
from utils.api import api_response, api_res_type

app = Flask(__name__)
app.register_blueprint(products_controller)

@app.route("/api/")
def hello():
    return get_products()
