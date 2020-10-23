import json

def get_products_stub():
    """
    :return: dictionary of generated products or None if file cannot be accessed
    """
    try:
        with open("stubs/products.json") as f:
            return json.load(f)
    except:
        return None


def create_products_stub(products):
    with open("stubs/products.json", 'w') as f:
        json.dump(products, f, indent=2)

def get_subscriptions_stub():
    """
    :return: dictionary of generated products or None if file cannot be accessed
    """
    try:
        with open("stubs/subscriptions.json") as f:
            return json.load(f)
    except:
        return None

def create_subscriptions_stub(subscriptions):
    with open("stubs/subscriptions.json", 'w') as f:
        json.dump(subscriptions, f, indent=2)
