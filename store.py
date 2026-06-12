import products


class Store:
    """Represents a store that contains products."""

    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
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


def main():
    """Test the Store class."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    product_items = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(product_items[0], 1), (product_items[1], 2)]))


if __name__ == "__main__":
    main()