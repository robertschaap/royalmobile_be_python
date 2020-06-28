from flask import Blueprint
from utils.api import ApiResponse
from utils.stubs import get_subscriptions_stub

subscriptions_controller = Blueprint('subscriptions_controller', __name__)

@subscriptions_controller.route('/api/subscriptions')
def get_subscriptions():
    try:
        subscriptions = get_subscriptions_stub()
        return ApiResponse.success(subscriptions)
    except:
        return ApiResponse.error("Subscriptions could not be found")
