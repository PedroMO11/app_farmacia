from app import db

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(8))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Product(db.Model):
    __tablename__ = 'products'
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    stock = db.Column(db.Integer)
    price = db.Column(db.Float)

    
    def __repr__(self):
        return '<Product {} {}>'.format(self.name, self.stock, self.price)


class Item():
    def __init__(self, code, quantity, price):
        self.code = code
        self.quantity = quantity
        self.price = price

    def update_stock(self):
        print("Updating stock of product {}".format(self.code))
        try:
            print("Before get product from DB")
            product = Product.query.get(self.code)
            print("After get product from DB")
            product.stock -= self.quantity
            if product.stock < 0:
                raise ValueError("Stock cannot be negative")
            print("New stock: {}".format(product.stock))
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()


class ShoppingCart():
    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price

    def finish_purchase(self):
        print("Finish purchase with total price of  {}".format(self.total_price))
        for item in self.items:
            item.update_stock()

    def __repr__(self):
        return '<ShoppingCart {} {}>'.format(self.products, self.total_price)