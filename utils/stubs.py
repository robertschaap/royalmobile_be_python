def get_products_stub():
    import json

    with open("stubs/products.json") as f:
        products_json = json.load(f)

    return products_json

def create_products_stub(products):
    import json

    with open("stubs/products.json", 'w') as f:
        json.dump(products, f, indent=2)

def get_subscriptions_stub():
    import json

    with open("stubs/subscriptions.json") as subscriptions_stub:
        subscriptions_json = subscriptions_stub.read()

    return json.loads(subscriptions_json)

def create_subscriptions_stub(subscriptions):
    import json

    with open("stubs/subscriptions.json", 'w') as f:
        json.dump(subscriptions, f, indent=2)
