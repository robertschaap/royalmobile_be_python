from db.cart import Cart
from db.products import Products
from db.subscriptions import Subscriptions

class Connection:
    carts = Cart()
    subscriptions = Subscriptions()
    products = Products()
