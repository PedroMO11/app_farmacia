from models import *
from app import *

shopping_cart = ShoppingCart([], 0)

@app.route('/')
def index():
    return render_template('index.html', products=Product.query.all())

#This route is going to be called within a Javascript function using query parameteres in the URL like this:
# /add_to_shopping_cart?productCode={productCode}&quantity={quantity}&unitPrice={unitPrice}

@app.route('/add_to_shopping_cart')
def add_to_shopping_cart():
    product_code = request.args.get('productCode')
    quantity = request.args.get('quantity')
    unit_price = request.args.get('unitPrice')
    item = Item(product_code, quantity)
    shopping_cart.items += [item]
    shopping_cart.total_price += (unit_price*quantity)
    #return #TODO: See if we can return something to be interpreted in the HTML page 


# This route is to finalize the purchase of the products selected in the shopping cart
@app.route('/shop')
def shop():
    shopping_cart.finish_purchase()
    #return #TODO: See if we can return something to be interpreted in the HTML page
