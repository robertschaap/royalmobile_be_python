from flask import Flask
from controllers.product import product_controller
from controllers.products import products_controller, get_products
from controllers.subscriptions import subscriptions_controller
from utils.api import ApiResponse

app = Flask(__name__)
app.register_blueprint(product_controller)
app.register_blueprint(products_controller)
app.register_blueprint(subscriptions_controller)

@app.route("/api/")
def hello():
    return ApiResponse.success('Hello world!')
