def product_factory(manufacturer, model, model_id):
    return {
        "id": 1,
        "manufacturer": manufacturer,
        "model": model,
        "modelId": model_id,
        "variants": [],
    }

def product_variant_factory(model_id, color, color_hex, capacity):
    return {
        "id": 1,
        "variantId": model_id + "-" + capacity + "-" + color,
        "color": color,
        "colorHex": color_hex,
        "capacity": capacity,
        "is_in_stock": True,
        "is_preorder": True,
        "regular_price": '265',
        "discounted_price": '239',
        "has_discounts": True,
    }

def create_product_stub(manufacturer, model, model_id):
    product = product_factory(manufacturer, model, model_id)

    product['variants'].append(product_variant_factory(product['modelId'], 'lime', '#7ec09a', '16gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'purple', '#8097c2', '16gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'green', '#bae596', '16gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'pink', '#d59a8d', '16gb'))

    product['variants'].append(product_variant_factory(product['modelId'], 'lime', '#7ec09a', '32gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'purple', '#8097c2', '32gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'green', '#bae596', '32gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'pink', '#d59a8d', '32gb'))

    product['variants'].append(product_variant_factory(product['modelId'], 'lime', '#7ec09a', '64gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'purple', '#8097c2', '64gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'green', '#bae596', '64gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'pink', '#d59a8d', '64gb'))

    product['variants'].append(product_variant_factory(product['modelId'], 'lime', '#7ec09a', '128gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'purple', '#8097c2', '128gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'green', '#bae596', '128gb'))
    product['variants'].append(product_variant_factory(product['modelId'], 'pink', '#d59a8d', '128gb'))

    return product

def get_products():
    products = []

    products.append(create_product_stub('Apple', 'iPhoneX1', 'apple-iphonex1'))
    products.append(create_product_stub('Apple', 'iPhoneX2', 'apple-iphonex2'))
    products.append(create_product_stub('Apple', 'iPhoneX3', 'apple-iphonex3'))
    products.append(create_product_stub('Apple', 'iPhoneX4', 'apple-iphonex4'))
    products.append(create_product_stub('Apple', 'iPhoneX5', 'apple-iphonex5'))
    products.append(create_product_stub('Apple', 'iPhoneX6', 'apple-iphonex6'))

    return products
