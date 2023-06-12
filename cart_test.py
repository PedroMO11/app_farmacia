import unittest
from models import ShoppingCart, Item, Product, User
from app import app, db

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.app_context().push()
        db.create_all()

        # Agrega ejemplos de usuarios y productos para las pruebas
        user = User(username='t', email='t@example.com', password='test')
        product = Product(code=30, name='Test', stock=10, price=9.99, img='50.jpg')
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        self.app = app.test_client()
        self.shopping_cart = ShoppingCart([], 0)

    def test_update_stock(self):
        # Crea un ítem de prueba
        item = Item(code=30, quantity=2)
        item.update_stock()

        # Verifica que el stock se haya actualizado correctamente
        updated_product = Product.query.get(30)
        self.assertEqual(updated_product.stock, 6)

    def test_finish_purchase(self):
        # Crea un ítem de prueba y agrega al carrito de compras
        item = Item(code=30, quantity=2)
        self.shopping_cart.items.append(item)

        # Finaliza la compra
        self.shopping_cart.finish_purchase()

        # Verifica que el stock se haya actualizado correctamente después de la compra
        updated_product = Product.query.get(30)
        self.assertEqual(updated_product.stock, 8)

if __name__ == '__main__':
    unittest.main()