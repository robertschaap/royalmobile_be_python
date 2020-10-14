class ProductFactory():
    __id = 0

    @classmethod
    def __get_id(cls):
        cls.__id += 1
        return cls.__id

    @classmethod
    def create(cls, manufacturer, model, model_id):
        return {
            'id': cls.__get_id(),
            'manufacturer': manufacturer,
            'model': model,
            'modelId': model_id,
            'variants': [],
        }


class ProductVariantFactory():
    __id = 0

    @classmethod
    def __get_id(cls):
        cls.__id += 1
        return cls.__id

    @classmethod
    def create(cls, model_id, color, color_hex, capacity):
        return {
            'id': cls.__get_id(),
            'variantId': model_id + "-" + capacity + "-" + color,
            'color': color,
            'colorHex': color_hex,
            'capacity': capacity,
            'is_in_stock': True,
            'is_preorder': True,
            'regular_price': "265",
            'discounted_price': "239",
            'has_discounts': True,
        }


def create_product(manufacturer, model, model_id):
    product = ProductFactory.create(manufacturer, model, model_id)

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#d8efd5', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'white', '#f5f5f7', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'red', '#d82e2e', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'black', '#25212b', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'blue', '#023b63', '64gb'))

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#d8efd5', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'white', '#f5f5f7', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'red', '#d82e2e', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'black', '#25212b', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'blue', '#023b63', '128gb'))

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#d8efd5', '256gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'white', '#f5f5f7', '256gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'red', '#d82e2e', '256gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'black', '#25212b', '256gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'blue', '#023b63', '256gb'))

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#d8efd5', '512gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'white', '#f5f5f7', '512gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'red', '#d82e2e', '512gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'black', '#25212b', '512gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'blue', '#023b63', '512gb'))

    return product

def create_products():
    products = []

    products.append(create_product('Apple', 'iPhone 12 v1', 'apple-iphone12v1'))
    products.append(create_product('Apple', 'iPhone 12 v2', 'apple-iphone12v2'))
    products.append(create_product('Apple', 'iPhone 12 v3', 'apple-iphone12v3'))
    products.append(create_product('Apple', 'iPhone 12 v4', 'apple-iphone12v4'))
    products.append(create_product('Apple', 'iPhone 12 v5', 'apple-iphone12v5'))
    products.append(create_product('Apple', 'iPhone 12 v6', 'apple-iphone12v6'))

    return products
