class ProductFactory():
    __id = 0

    @classmethod
    def __get_id(self):
        self.__id += 1
        return self.__id

    @classmethod
    def create(self, manufacturer, model, model_id):
        return {
            'id': self.__get_id(),
            'manufacturer': manufacturer,
            'model': model,
            'modelId': model_id,
            'variants': [],
        }


class ProductVariantFactory():
    __id = 0

    @classmethod
    def __get_id(self):
        self.__id += 1
        return self.__id

    @classmethod
    def create(self, model_id, color, color_hex, capacity):
        return {
            'id': self.__get_id(),
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


def get_product(manufacturer, model, model_id):
    product = ProductFactory.create(manufacturer, model, model_id)

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'lime', '#7ec09a', '16gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'purple', '#8097c2', '16gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#bae596', '16gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'pink', '#d59a8d', '16gb'))

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'lime', '#7ec09a', '32gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'purple', '#8097c2', '32gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#bae596', '32gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'pink', '#d59a8d', '32gb'))

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'lime', '#7ec09a', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'purple', '#8097c2', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#bae596', '64gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'pink', '#d59a8d', '64gb'))

    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'lime', '#7ec09a', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'purple', '#8097c2', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'green', '#bae596', '128gb'))
    product['variants'].append(ProductVariantFactory.create(product['modelId'], 'pink', '#d59a8d', '128gb'))

    return product

def get_products():
    products = []

    products.append(get_product('Apple', 'iPhone X1', 'apple-iphonex1'))
    products.append(get_product('Apple', 'iPhone X2', 'apple-iphonex2'))
    products.append(get_product('Apple', 'iPhone X3', 'apple-iphonex3'))
    products.append(get_product('Apple', 'iPhone X4', 'apple-iphonex4'))
    products.append(get_product('Apple', 'iPhone X5', 'apple-iphonex5'))
    products.append(get_product('Apple', 'iPhone X6', 'apple-iphonex6'))

    return products
