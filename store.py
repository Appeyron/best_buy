"""Store module.

Provides the Store class for managing products and orders.
"""

import products


class Store:
    """Represents a store that contains products."""

    def __init__(self, product_list):
        if not isinstance(product_list, list):
            raise TypeError("product_list must be a list.")

        for product in product_list:
            if not isinstance(product, products.Product):
                raise TypeError(
                    "All items in product_list must be Product instances."
                )

        self.products = product_list

    def add_product(self, product):
        if not isinstance(product, products.Product):
            raise TypeError("product must be a Product instance.")

        self.products.append(product)

    def remove_product(self, product):
        if not isinstance(product, products.Product):
            raise TypeError("product must be a Product instance.")

        if product not in self.products:
            raise ValueError("Product not found in store.")

        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products."""
        total = 0

        for product in self.products:
            total += product.get_quantity()

        return total

    def get_all_products(self):
        """Return all active products."""
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        """Buy multiple products and return total order price."""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
