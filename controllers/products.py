from flask import Blueprint
from utils.api import api_response, api_res_type

products_controller = Blueprint('products_controller', __name__)

def get_products_stub():
    import json

    with open("stubs/products.json") as products_stub:
        products_json = products_stub.read()

    return json.loads(products_json)

@products_controller.route('/api/products')
def get_products():
    return api_response(
        api_res_type["success"],
        get_products_stub(),
    )
