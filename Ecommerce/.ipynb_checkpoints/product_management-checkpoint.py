# ecommerce/product_management.py

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """Update product stock."""
        self.stock += quantity
        return f"Updated stock for {self.name}: {self.stock}"

    def get_product_info(self):
        """Return product details."""
        return f"ID: {self.product_id}, Name: {self.name}, Price: ₹{self.price}, Stock: {self.stock}"
