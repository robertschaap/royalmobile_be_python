from utils.stubs import create_products_stub, create_subscriptions_stub
from stubs.products import get_products
from stubs.subscriptions import get_subscriptions

products = get_products()
create_products_stub(products)

subscriptions = get_subscriptions()
create_subscriptions_stub(subscriptions)
