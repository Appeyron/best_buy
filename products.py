"""Product module.

Provides the Product class for managing store inventory.
"""


class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product."""

        # Type checks
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        # Value checks
        if not name.strip():
            raise ValueError("Name cannot be empty.")

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
        """Set the quantity of the product."""

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

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
        """Return a string representation of the product."""
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Purchase a quantity of the product.

        Args:
            quantity (int): The amount of the product to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            TypeError: If quantity is not an integer.
            ValueError: If the product is inactive, quantity is less than
                        or equal to zero, or stock is insufficient.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if not self.is_active():
            raise ValueError("Product is inactive.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > self.quantity:
            raise ValueError("Not enough items in stock.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        return total_price
