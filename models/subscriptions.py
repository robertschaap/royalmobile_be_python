from utils.stubs import get_subscriptions_stub
from db import Connection

class SubscriptionsModel:
    def get_subscriptions(self):
        return Connection.subscriptions.get_subscriptions()
