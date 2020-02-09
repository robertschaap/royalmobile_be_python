from flask import Blueprint
from utils.api import api_response, api_res_type

subscriptions_controller = Blueprint('subscriptions_controller', __name__)

def get_subscriptions_stub():
    import json

    with open("stubs/subscriptions.json") as subscriptions_stub:
        subscriptions_json = subscriptions_stub.read()

    return json.loads(subscriptions_json)

@subscriptions_controller.route('/api/subscriptions')
def get_subscriptions():
    return api_response(
        api_res_type["success"],
        get_subscriptions_stub(),
    )
