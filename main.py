import products
import store


def start(best_buy):
    """Display the store menu."""

    print("Store Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def main():
    """Initialize store."""

    product_list = [
        products.Product(
            "MacBook Air M2",
            price=1450,
            quantity=100
        ),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500
        ),
        products.Product(
            "Google Pixel 7",
            price=500,
            quantity=250
        )
    ]

    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()