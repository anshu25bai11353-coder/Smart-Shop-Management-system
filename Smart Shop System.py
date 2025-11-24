
# --- Initial Inventory ---
inventory = {
    "Pen": {"price": 10, "qty": 20},
    "Notebook": {"price": 50, "qty": 8},
    "Pencil": {"price": 5, "qty": 100},
    "Rubber": {"price": 10, "qty": 100},
    "Calculator": {"price": 100, "qty": 100}
}
sales = []

# =================================================================
# MODULE 1: OWNER FUNCTIONS (Inventory Management)
# =================================================================

def add_new_product(inventory):
    """Handles the addition of a new product to the inventory."""
    print("\n--- Add New Product ---")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price (₹): "))
    qty = int(input("Enter Quantity: "))
    # Correct application of data structures and logic
    inventory[name] = {"price": price, "qty": qty}
    print("Product Added Successfully!")

def update_existing_product(inventory):
    """Handles the update (stock addition) of an existing product."""
    print("\n--- Update Existing Product ---")
    name = input("Enter Product to Update: ")
    if name in inventory:
        new_qty = int(input("Enter Quantity to Add: "))
        inventory[name]["qty"] += new_qty
        print("Quantity Updated!")
        # Error handling & usability alert
        if inventory[name]["qty"] <= 5:
            print("ALERT: Product stock is VERY LOW (≤5)")
    else:
        # Validation and error handling
        print("Product not found!")

def view_inventory(inventory):
    """Displays the current state of the inventory."""
    print("\n------ CURRENT INVENTORY ------")
    # Correct application of algorithms (iteration)
    for item, d in inventory.items():
        print(f"{item} -> Price: ₹{d['price']} | Qty: {d['qty']}")

def owner_panel(inventory, password_check="1234"):
    """Main loop for the Owner section."""
    password = input("Enter Owner Password: ")

    if password == password_check:
        print("\nOwner Login Successful!")
        print("===== INVENTORY MANAGEMENT =====")

        while True:
            print("\n1. Add New Product")
            print("2. Update Existing Product")
            print("3. View Inventory")
            print("4. Exit Owner Panel")

            owner_choice = input("Enter choice: ")

            if owner_choice == "1":
                add_new_product(inventory)
            elif owner_choice == "2":
                update_existing_product(inventory)
            elif owner_choice == "3":
                view_inventory(inventory)
            elif owner_choice == "4":
                break
            else:
                # Error handling
                print("Invalid choice!")
    else:
        # Security validation and error handling
        print("Wrong Password! Access Denied.")
        exit()

# =================================================================
# MODULE 2: CUSTOMER FUNCTIONS (Billing and Transaction)
# =================================================================

def display_available_products(inventory):
    """Displays products for the customer."""
    print("\n===== CUSTOMER BILLING SECTION =====")
    print("Available Products:")
    for item, d in inventory.items():
        print(f"{item} - Price: ₹{d['price']} | Qty: {d['qty']}")

def customer_billing_process(inventory, sales):
    """Handles the main customer purchasing loop."""
    cart = []     # multiple items
    
    display_available_products(inventory)

    while True:
        product = input("\nEnter product to buy: ")

        if product in inventory:
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue

            # Validation and error handling (Stock check)
            if quantity <= inventory[product]["qty"]:
                # Correct application of algorithms (Price calculation)
                price = inventory[product]["price"] * quantity
                gst = price * 0.18
                total = price + gst

                # Update stock
                inventory[product]["qty"] -= quantity

                # Usability alert
                if inventory[product]["qty"] <= 5:
                    print(" ALERT: LOW STOCK for", product)

                # Add to cart and sales
                cart.append((product, quantity, price, gst, total))
                sales.append({"product": product, "qty": quantity, "total": total})

                more_buy = input("Anything else? (yes/no): ")
                if more_buy.lower() == "no":
                    break
            else:
                # Error handling (Insufficient stock)
                print("Not enough stock!")
        else:
            # Error handling (Product not found)
            print("Product not found!")

    return cart

# =================================================================
# MODULE 3: REPORTING FUNCTIONS (Bill Print and Sales Report)
# =================================================================

def print_final_bill(cart):
    """Calculates and prints the final customer bill."""
    total_bill = 0
    total_gst = 0

    print("\n=============================== FINAL BILL ==============================================================")

    # Correct application of algorithms (Bill aggregation)
    for item in cart:
        print(f"| Product: {item[0]} | Qty: {item[1]} | Amount: ₹{item[2]} | GST: ₹{item[3]} | Total: ₹{item[4]} |")
        total_bill += item[4]
        total_gst += item[3]

    # Correct application of algorithms (Discount)
    # The original code calculates discount on the GST-inclusive total_bill.
    discount = total_bill * 0.10
    amount_after_discount = total_bill - discount

    print("----------------------------------------------------------------------------------------------------------")
    print(" Total GST Collected : ₹", round(total_gst, 2))
    print(" Total Amount (Before Discount): ₹", round(total_bill, 2))
    print(" Discount (10%): ₹", round(discount, 2))
    print("                                ")
    print(" Final Amount Payable: ₹", round(amount_after_discount, 2))
    print("===========================================================================================================")

def print_sales_report(sales):
    """Prints the sales transactions recorded during the session."""
    print("\n===== SALES REPORT =====")
    if len(sales) == 0:
        print("No sales recorded.")
    else:
        for s in sales:
            print(f"{s['product']} | Qty: {s['qty']} | Amount: ₹{s['total']}")
    print("\nThank you for shopping! 😊")

# =================================================================
# MAIN EXECUTION LOGIC (Logical Workflow)
# =================================================================

print("============= WELCOME TO SMART SHOP SYSTEM =============")

print("\n1. Owner")
print("2. Customer")

role = input("Choose your role (1/2): ")

if role == "1":
    owner_panel(inventory)
elif role == "2":
    customer_cart = customer_billing_process(inventory, sales)
    # Only proceed to billing/reporting if items were added to the cart
    if customer_cart:
        print_final_bill(customer_cart)
        print_sales_report(sales)
else:
    print("Invalid role choice. Exiting.")

# End of main execution.
