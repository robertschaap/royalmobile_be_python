from flask import Blueprint
from utils.api import ApiResponse
from models.subscriptions import SubscriptionsModel

subscriptions_controller = Blueprint('subscriptions_controller', __name__)
subscriptions_model = SubscriptionsModel()

@subscriptions_controller.route('/api/subscriptions')
def get_subscriptions():
    subscriptions = subscriptions_model.get_subscriptions()
    return ApiResponse.success(subscriptions)
