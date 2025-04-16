# ecommerce/order_processing.py
# from ecommerce.product_management import Product

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = "Pending"

    def process_order(self):
        """Process the order and update stock."""
        if self.product.stock >= self.quantity:
            self.product.stock -= self.quantity
            self.status = "Completed"
            return f"Order {self.order_id} completed. Remaining stock: {self.product.stock}"
        else:
            self.status = "Failed"
            return f"Order {self.order_id} failed. Not enough stock."

    def get_order_details(self):
        """Return order details."""
        return f"Order ID: {self.order_id}, Product: {self.product.name}, Quantity: {self.quantity}, Status: {self.status}"
