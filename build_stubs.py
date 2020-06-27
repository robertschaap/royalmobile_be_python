from utils.stubs import create_products_stub
from stubs.products import get_products

products = get_products()
create_products_stub(products)
