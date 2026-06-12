class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """
        Initialize a product.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Available quantity.

        Raises:
            ValueError: If name is empty or price/quantity is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the available quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set a new quantity.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print product information."""
        print(
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )

    def buy(self, quantity):
        """
        Buy a given quantity of the product.

        Args:
            quantity (int): Amount to buy.

        Returns:
            float: Total purchase price.

        Raises:
            ValueError: If quantity is invalid or unavailable.
        """
        if quantity <= 0:
            raise ValueError(
                "Purchase quantity must be greater than zero."
            )

        if quantity > self.quantity:
            raise ValueError(
                "Not enough items available in stock."
            )

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price


# def main():
#     """Test the Product class."""
#     bose = Product(
#         "Bose QuietComfort Earbuds",
#         price=250,
#         quantity=500
#     )
#
#     mac = Product(
#         "MacBook Air M2",
#         price=1450,
#         quantity=100
#     )
#
#     print(bose.buy(50))
#     print(mac.buy(100))
#     print(mac.is_active())
#
#     bose.show()
#     mac.show()
#
#     bose.set_quantity(1000)
#     bose.show()
#
#
# if __name__ == "__main__":
#     main()