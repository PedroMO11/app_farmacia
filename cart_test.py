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
        product = Product(code=30, name='Test', stock=10, price=9.99)
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

    def test_add_to_shopping_cart_product_not_found(self):
        # Hace una solicitud a la ruta '/add_to_shopping_cart' con un producto no existente
        response = self.app.get('/add_to_shopping_cart?productCode=9999&quantity=2&unitPrice=9.99')

        # Verifica que la respuesta sea un código 404 (not found)
        self.assertEqual(response.status_code, 404)

        # Verifica que el carrito de compras no se haya modificado
        self.assertEqual(len(self.shopping_cart.items), 0)
        self.assertEqual(self.shopping_cart.total_price, 0)

    def test_finish_purchase(self):
        # Crea un ítem de prueba y agrega al carrito de compras
        item = Item(code=30, quantity=2)
        self.shopping_cart.items.append(item)

        # Finaliza la compra
        self.shopping_cart.finish_purchase()

        # Verifica que el stock se haya actualizado correctamente después de la compra
        updated_product = Product.query.get(30)
        self.assertEqual(updated_product.stock, 8)

    def test_update_stock_negative(self):
    # Crea un ítem de prueba con una cantidad mayor al stock disponible
        item = Item(code=30, quantity=20)

        with self.assertRaises(ValueError) as cm:
            item.update_stock()

        self.assertEqual(str(cm.exception), "Insufficient stock")


if __name__ == '__main__':
    unittest.main()