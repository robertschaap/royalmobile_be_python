import json

def get_products_stub():
    """
    :return: list of generated products or None if file cannot be accessed
    """
    try:
        with open("stubs/products.json") as f:
            return json.load(f)
    except:
        return None


def create_products_stub(products):
    """
    Saves created products stub to file or prints error message
    """
    try:
        with open("stubs/products.json", 'w') as f:
            json.dump(products, f, indent=2)
    except:
        print("Could not create products stub")

def get_subscriptions_stub():
    """
    :return: list of generated subscriptions or None if file cannot be accessed
    """
    try:
        with open("stubs/subscriptions.json") as f:
            return json.load(f)
    except:
        return None

def create_subscriptions_stub(subscriptions):
    """
    Saves created subscriptions stub to file or prints error message
    """
    try:
        with open("stubs/subscriptions.json", 'w') as f:
            json.dump(subscriptions, f, indent=2)
    except:
        print("Could not create subscriptions stub")
