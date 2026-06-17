"""Best Buy store application.

Provides a command-line interface for browsing products,
viewing inventory, and placing orders.
"""

import products
import store


def list_products(best_buy):
    """List all active products."""
    print("------")
    for index, product in enumerate(best_buy.get_all_products(), start=1):
        print(f"{index}. {product.show()}")
    print("------")


def show_total_amount(best_buy):
    """Show total quantity in store."""
    total = best_buy.get_total_quantity()
    print(f"Total of {total} items in store")


def make_order(best_buy):
    """Handle order creation with input validation and navigation shortcuts."""
    print("\n--- New Order ---")

    # Initial list display
    list_products(best_buy)
    print("Enter product # to add to order, 'l' to see the list, or Enter to finish.")

    product_list = best_buy.get_all_products()
    shopping_list = []

    while True:
        user_input = input("\nWhich product # do you want? "
                           "(Enter = finish, 'l' = list products): ").strip().lower()

        # 1. Exit condition
        if not user_input:
            break

        # 2. List products shortcut
        if user_input == 'l':
            list_products(best_buy)
            continue

        # 3. Product Selection
        try:
            product_index = int(user_input) - 1
            if not (0 <= product_index < len(product_list)):
                print("Invalid product number.")
                continue
        except ValueError:
            print("Please enter a valid number or 'l' to list products.")
            continue

        # 4. Quantity Selection
        try:
            qty_input = input(f"How many units of '{product_list[product_index].name}'? ").strip()
            quantity = int(qty_input)

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            shopping_list.append((product_list[product_index], quantity))
            print("Product added to list!")

        except ValueError:
            print("Please enter a valid number for the quantity.")

    # 5. Finalize Order
    if not shopping_list:
        print("Order cancelled (no items selected).")
        return

    try:
        total_price = best_buy.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price:.2f}")
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

    while True:
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

        if action(best_buy) is False:
            break


def main():
    """Initialize store and start menu."""
    try:
        product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250),
        ]

        best_buy = store.Store(product_list)
        start(best_buy)

    except (ValueError, TypeError) as error:
        print(f"Initialization error: {error}")


if __name__ == "__main__":
    main()
