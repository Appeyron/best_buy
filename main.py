"""Best Buy store application.

Provides a command-line interface for browsing products,
viewing inventory, and placing orders.
"""

import products
import store


def list_products(best_buy):
    """List all active products."""

    print("------")

    for index, product in enumerate(
        best_buy.get_all_products(),
        start=1
    ):
        print(f"{index}. {product.show()}")

    print("------")


def show_total_amount(best_buy):
    """Show total quantity in store."""

    total = best_buy.get_total_quantity()

    print(f"Total of {total} items in store")


def make_order(best_buy):
    """Make an order."""

    print("------")

    products_list = best_buy.get_all_products()

    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product.show()}")

    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        try:
            product_number = input(
                "Which product # do you want? "
            ).strip()

            if product_number == "":
                input("What amount do you want? ")
                break

            product_index = int(product_number) - 1

            if (
                product_index < 0
                or product_index >= len(products_list)
            ):
                print("Invalid product number.\n")
                continue

            quantity = int(
                input("What amount do you want? ")
            )

            product = products_list[product_index]

            shopping_list.append(
                (product, quantity)
            )

            print("Product added to list!\n")

        except ValueError:
            print(
                "Please enter a valid number.\n"
            )

    try:
        total_price = best_buy.order(shopping_list)

        print("********")
        print(
            f"Order made! "
            f"Total payment: ${total_price}"
        )

    except ValueError as error:
        print(f"Order failed: {error}")


def quit_program(_best_buy):
    """Quit application."""

    print("Goodbye!")
    return False


def start(best_buy):
    """Display and handle menu."""

    menu_actions = {
        "1": list_products,
        "2": show_total_amount,
        "3": make_order,
        "4": quit_program,
    }

    running = True

    while running:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        action = menu_actions.get(choice)

        if action is None:
            print("Invalid choice.")
            continue

        result = action(best_buy)

        if result is False:
            running = False


def main():
    """Initialize store and start menu."""

    try:
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

    except ValueError as error:
        print(f"Application error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
