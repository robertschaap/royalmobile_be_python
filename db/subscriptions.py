from utils.stubs import get_subscriptions_stub

class Subscriptions:
    def get_subscriptions(self):
        return get_subscriptions_stub or []

    def get_subscription_by_id(self, subscription_id):
        subscriptions = get_subscriptions_stub or []

        return next((x for x in subscriptions if x["subscriptionId"] == subscription_id), None)
