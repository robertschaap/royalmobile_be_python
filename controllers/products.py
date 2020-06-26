from flask import Blueprint
from utils.api import api_response, api_res_type
from utils.stubs import get_products_stub

products_controller = Blueprint('products_controller', __name__)

@products_controller.route('/api/products')
def get_products():
    return api_response(
        api_res_type["success"],
        get_products_stub(),
    )
