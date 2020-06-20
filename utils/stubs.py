def get_products_stub():
    import json

    with open("stubs/products.json") as f:
        products_json = json.load(f)

    return products_json

def get_subscriptions_stub():
    import json

    with open("stubs/subscriptions.json") as subscriptions_stub:
        subscriptions_json = subscriptions_stub.read()

    return json.loads(subscriptions_json)
