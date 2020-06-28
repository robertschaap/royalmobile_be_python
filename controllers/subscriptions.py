from flask import Blueprint
from utils.api import api_response, api_res_type
from utils.stubs import get_subscriptions_stub

subscriptions_controller = Blueprint('subscriptions_controller', __name__)

@subscriptions_controller.route('/api/subscriptions')
def get_subscriptions():
    try:
        return api_response(
            api_res_type["success"],
            get_subscriptions_stub(),
        )
    except:
        return api_response(
            api_res_type["error"],
            None,
            "Subscriptions could not be found"
        )
