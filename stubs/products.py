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

    colors = {
        'green': "#d8efd5",
        'white': "#f5f5f7",
        'red': "#d82e2e",
        'black': "#25212b",
        'blue': "#023b63",
    }

    capacities = ['64gb', '128gb', '256gb', '512gb']

    for capacity in capacities:
        for color, hex_code in colors.items():
            product['variants'].append(ProductVariantFactory.create(product['modelId'], color, hex_code, capacity))

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
