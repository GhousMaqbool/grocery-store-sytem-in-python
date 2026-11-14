"""Smart Grocery Store Management System.

A console application that manages products, stock, customer sales and
store reports using lists of dictionaries.
"""

LOW_STOCK_LIMIT = 5

# Main data structures: a list of product dictionaries and a list of sale dictionaries
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120, "stock": 4},
    {"id": 103, "name": "Rice", "category": "Grains", "price": 480, "stock": 50},
]
sales = []


# ---------- Input helper functions ----------

def get_int(prompt, minimum=0):
    """Ask until the user enters a whole number >= minimum."""
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) >= minimum:
            return int(raw)
        print(f"Invalid input. Enter a whole number (minimum {minimum}).")


def get_price(prompt):
    """Ask until the user enters a number greater than 0."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input. Enter a number, e.g. 250 or 99.5.")
            continue
        if value > 0:
            return value
        print("Price must be greater than 0.")


def get_text(prompt):
    """Ask until the user enters non-empty text; returns it in Title Case."""
    while True:
        text = input(prompt).strip().title()
        if text:
            return text
        print("This field cannot be empty.")


# ---------- Product lookup helpers ----------

def find_product_by_id(product_id):
    """Return the product dictionary with the given ID, or None if not found."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def print_product(product):
    """Print the complete details of one product."""
    print(f"  ID: {product['id']} | Name: {product['name']} | "
          f"Category: {product['category']} | "
          f"Price: Rs. {product['price']:.2f} | Stock: {product['stock']}")


# ---------- Menu operations ----------

def add_product():
    """Add a new product after making sure its ID is unique."""
    print("\n--- Add New Product ---")
    while True:
        product_id = get_int("Enter product ID: ", 1)
        if find_product_by_id(product_id) is None:
            break
        print("This product ID already exists. Please use a different ID.")

    name = get_text("Enter product name: ")
    category = get_text("Enter category: ")
    price = get_price("Enter price: ")
    stock = get_int("Enter available stock: ", 0)

    new_product = {"id": product_id, "name": name, "category": category,
                   "price": price, "stock": stock}
    products.append(new_product)  # store the dictionary in the list
    print(f"Product '{name}' added successfully.")


def view_products():
    """Display every product in a readable table."""
    print("\n--- All Products ---")
    if len(products) == 0:
        print("No products available.")
        return
    print(f"{'ID':<6}{'Name':<18}{'Category':<14}{'Price':>10}{'Stock':>8}")
    print("-" * 56)
    for product in products:
        print(f"{product['id']:<6}{product['name']:<18}{product['category']:<14}"
              f"{product['price']:>10.2f}{product['stock']:>8}")


def search_product():
    """Search products by ID (digits) or by name (case-insensitive, partial match)."""
    print("\n--- Search Product ---")
    query = input("Enter product name or ID: ").strip()
    if query == "":
        print("Search cannot be empty.")
        return

    found = []
    if query.isdigit():
        match = find_product_by_id(int(query))
        if match is not None:
            found.append(match)
    else:
        for product in products:
            if query.lower() in product["name"].lower():
                found.append(product)

    if len(found) == 0:
        print("Product not found.")
    else:
        print(f"{len(found)} product(s) found:")
        for product in found:
            print_product(product)


def update_stock():
    """Add to or replace the stock quantity of an existing product."""
    print("\n--- Update Product Stock ---")
    product_id = get_int("Enter product ID: ", 1)
    product = find_product_by_id(product_id)
    if product is None:
        print("Product not found.")
        return

    print(f"Current stock of {product['name']}: {product['stock']}")
    print("1. Add stock")
    print("2. Set new quantity")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        product["stock"] += get_int("Enter quantity to add: ", 1)
    elif choice == "2":
        product["stock"] = get_int("Enter new stock quantity: ", 0)
    else:
        print("Invalid option. Stock was not changed.")
        return

    print("Stock updated:")
    print_product(product)


def process_sale():
    """Sell a product: check stock, deduct quantity, and record the sale."""
    print("\n--- Process Customer Sale ---")
    product_id = get_int("Enter product ID: ", 1)
    product = find_product_by_id(product_id)
    if product is None:
        print("Product not found.")
        return

    print(f"{product['name']} - Price: Rs. {product['price']:.2f}, "
          f"Available: {product['stock']}")
    quantity = get_int("Enter quantity to purchase: ", 1)

    # Do not allow the sale if stock is not enough
    if quantity > product["stock"]:
        print(f"Sale denied. Only {product['stock']} unit(s) available.")
        return

    total = quantity * product["price"]
    product["stock"] -= quantity  # deduct purchased quantity

    sales.append({"id": product["id"], "name": product["name"],
                  "quantity": quantity, "total": total})

    print("\n----- Purchase Summary -----")
    print(f"Product   : {product['name']}")
    print(f"Quantity  : {quantity}")
    print(f"Unit price: Rs. {product['price']:.2f}")
    print(f"Total     : Rs. {total:.2f}")
    print(f"Remaining stock: {product['stock']}")


def view_sales():
    """Display all completed sales records."""
    print("\n--- Sales Records ---")
    if len(sales) == 0:
        print("No sales recorded yet.")
        return
    print(f"{'#':<4}{'ID':<6}{'Name':<18}{'Qty':>6}{'Total':>12}")
    print("-" * 46)
    for number, sale in enumerate(sales, start=1):
        print(f"{number:<4}{sale['id']:<6}{sale['name']:<18}"
              f"{sale['quantity']:>6}{sale['total']:>12.2f}")


def generate_report():
    """Display store totals, low-stock items and highest/lowest priced products."""
    print("\n========== STORE REPORT ==========")
    total_stock = 0
    for product in products:
        total_stock += product["stock"]

    total_revenue = 0
    for sale in sales:
        total_revenue += sale["total"]

    print(f"Total products          : {len(products)}")
    print(f"Total available stock   : {total_stock}")
    print(f"Total sales transactions: {len(sales)}")
    print(f"Total revenue           : Rs. {total_revenue:.2f}")

    # Products running low on stock
    print(f"\nProducts with stock below {LOW_STOCK_LIMIT}:")
    low_found = False
    for product in products:
        if product["stock"] < LOW_STOCK_LIMIT:
            print(f"  {product['name']} (ID {product['id']}) - stock: {product['stock']}")
            low_found = True
    if not low_found:
        print("  None")

    # Highest and lowest priced products
    if len(products) > 0:
        highest = products[0]
        lowest = products[0]
        for product in products:
            if product["price"] > highest["price"]:
                highest = product
            if product["price"] < lowest["price"]:
                lowest = product
        print(f"\nHighest priced: {highest['name']} (Rs. {highest['price']:.2f})")
        print(f"Lowest priced : {lowest['name']} (Rs. {lowest['price']:.2f})")
    print("==================================")


def show_menu():
    """Print the main menu."""
    print("\n====================================")
    print("SMART GROCERY STORE SYSTEM")
    print("====================================\n")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit\n")


def main():
    """Run the menu loop until the user chooses Exit."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            process_sale()
        elif choice == "6":
            view_sales()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
