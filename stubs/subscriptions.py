class SubscriptionFactory():
    __id = 0

    @classmethod
    def __get_id(self):
        self.__id += 1
        return self.__id

    @classmethod
    def create(self, capacity, duration, price):
        return {
            'id': self.__get_id(),
            'subscriptionId': "royalmobile-" + capacity + "-" + duration,
            'durationId': duration,
            'data': capacity,
            'benefits_long': [
                "unlimited calls",
                "unlimited texts",
                "unlimited roaming"
            ],
            'benefits_short': "unlimited\n calls, texts, roaming",
            'regular_price': price
        }

def get_subscriptions():
    subscriptions = []

    subscriptions.append(SubscriptionFactory.create("20gb", "1year", "20"))
    subscriptions.append(SubscriptionFactory.create("40gb", "1year", "30"))
    subscriptions.append(SubscriptionFactory.create("60gb", "1year", "40"))
    subscriptions.append(SubscriptionFactory.create("80gb", "1year", "50"))
    subscriptions.append(SubscriptionFactory.create("20gb", "2year", "18"))
    subscriptions.append(SubscriptionFactory.create("40gb", "2year", "28"))
    subscriptions.append(SubscriptionFactory.create("60gb", "2year", "38"))
    subscriptions.append(SubscriptionFactory.create("80gb", "2year", "48"))

    return subscriptions
