from prettytable import PrettyTable, ALL
import json

# Load products from a JSON file
with open("products.json", "r") as product:
    products = json.load(product)

# Function to display a table of products
def display_table(data, field_names):
    table = PrettyTable()
    table.field_names = field_names
    table.hrules = ALL
    for item in data:
        table.add_row(item)
    print(table)

# Function to display all products
def display_products(display_name):
    product_data = [
        [
            product["product_id"],
            product["name"].title(),
            product["category"].title(),
            f"${product['price']:.2f}",
            f"{product['stock_quantity']} PC"
        ]
        for product in display_name
    ]
    display_table(product_data, ["Product ID", "Name", "Category", "Price", "Stock Quantity"])

# Show all products
def show_all_products():
    display_products(products)

# Function to get user input with a fallback to None if empty
def get_input(prompt):
    return input(prompt).strip() or None

# Add a new product to the list
def add_new_product():
    category = input("Category: ")
    if not category:
        print("Please add a Category!")
        return

    name_product = input("Product Name: ")
    if not name_product:
        print("Please add a product name!")
        return

    price = get_input("Price: ")
    if price:
        try:
            price = float(price)
        except ValueError:
            print("Please add the price correctly.")
            return

    stock_quantity = get_input("Stock Quantity: ")
    if stock_quantity:
        try:
            stock_quantity = int(stock_quantity)
        except ValueError:
            print("Please add the stock quantity correctly.")
            return

    new_product = {
        "product_id": len(products) + 1,
        "name": name_product,
        "category": category,
        "price": price,
        "stock_quantity": stock_quantity
    }

    products.append(new_product)
    print("Product added successfully!")

# Function to find a product by ID or name
def find_product(user_input):
    work = False
    found_products = []
    for product in products:
        if str(product["product_id"]) == user_input or user_input == product["name"].lower():
            found_products.append([
                product["product_id"],
                product["name"].title(),
                product["category"].title(),
                f"${product['price']:.2f}",
                f"{product['stock_quantity']} PC"
            ])
            work = True
    if work:
        display_table(found_products, ["Product ID", "Name", "Category", "Price", "Stock Quantity"])
    return work

# Function to update product details
def update_product(user_input):
    update = next((product for product in products if str(product["product_id"]) == user_input or user_input == product["name"].lower()), None)
    if update:
        print("Press Enter to skip any value.")
        name = input(f"Product Name ({update['name']}): ").title() or update["name"]
        category = input(f"Category Name ({update['category']}): ").title() or update["category"]
        price_input = input(f"Price ({update['price']}): ").strip()
        stock_input = input(f"Stock Quantity ({update['stock_quantity']}): ").strip()

        if price_input:
            try:
                price = float(price_input)
            except ValueError:
                price = update["price"]
        else:
            price = update["price"]

        if stock_input:
            try:
                stock = int(stock_input)
            except ValueError:
                stock = update["stock_quantity"]
        else:
            stock = update["stock_quantity"]

        update["name"] = name
        update["category"] = category
        update["price"] = price
        update["stock_quantity"] = stock

        print("\nUpdated Product Details:")
        display_table([[update["product_id"], update["name"], update["category"], f"${update['price']:.2f}", f"{update['stock_quantity']} PC"]],
                      ["Product ID", "Name", "Category", "Price", "Stock Quantity"])
    else:
        print("That product was not found.")

# Function to display analysis of stock quantities
def analysis_quantity():
    product_data = [
        [item["name"], f"{item['stock_quantity']} PC"] for item in products
    ]
    display_table(product_data, ["Name", "Stock Quantity"])

# Function to display low inventory products
def low_inventory():
    low_stock_products = [
        [item["name"], f"{item['stock_quantity']} PC"] for item in products if item["stock_quantity"] < 50
    ]
    display_table(low_stock_products, ["Product", "Stock Quantity"])

# Function to process sale of products
def sale_products(name, count):
    found = False
    for item in products:
        if name == item["name"].lower() or str(item["product_id"]) == name:
            item["stock_quantity"] -= count
            print("Update Successful!")
            found = True
    return found

# Login process
log_in = [
    {"M": "1"},
    {"Mahmoud Ibrahim": "12345d"}
]

user_name = input("Enter Your Name: ").strip()
password = input("Enter Your Password: ")

work = False

for login in log_in:
    for key, value in login.items():
        if key == user_name.title() and value == password:
            print("Welcome to Store Management.")
            work = True

if not work:
    print("Sorry, you can't login.")

while work:
    print("""
    1- Show All Products
    2- Search for Product
    3- Add a New Product
    4- Update Product
    5- Display Stock Quantity
    6- Low Inventory
    7- Add Sales
    8- Exit
    """)

    user_choice = input("Choose an option: ").strip()

    if user_choice == "1":
        show_all_products()
    elif user_choice == "2":
        user_search = input("Enter product details: ").strip().lower()
        if not find_product(user_search):
            print("Product not found!")
    elif user_choice == "3":
        add_new_product()
    elif user_choice == "4":
        user_update = input("Enter product details to update: ").strip().lower()
        update_product(user_update)
    elif user_choice == "5":
        analysis_quantity()
    elif user_choice == "6":
        low_inventory()
    elif user_choice == "7":
        name = input("Enter product name or ID: ").lower().strip()
        count = int(input("How many sold: "))
        if not sale_products(name, count):
            print("Product not found or invalid quantity!")
    elif user_choice == "8":
        print("Goodbye!")
        work = False
    else:
        print("Please choose a valid option (1-8).")


