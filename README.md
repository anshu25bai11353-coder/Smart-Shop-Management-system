# Smart-Shop-Management-system

A Python-based Smart Shop Management System under the domain of retail & E-commerce featuring inventory control, owner authentication, product updates, low-stock alerts, customer purchasing, GST billing, and sales reporting. Designed for real-world retail scenarios and developed as a flipped course project with clean structure and documentation. This retail management project designed to simplify day-to-day shop operations including inventory control, billing, GST calculation, product search, and customer-friendly checkout. This system provides a clean, menu-driven interface suitable for small and medium shops.

# Overview:

The Smart Shop Management System is a practical Python project built to mimic real retail workflows.  
It helps shopkeepers manage stock, generate bills, maintain pricing with GST, track sales, and interact with the system through a command-line interface.

This project demonstrates key programming concepts including:
- Modular development  
- Dictionaries & lists  
- Menu-driven control flow  
- Functions  
- Error handling  
- Real-world logic building  

# Objectives:

- Build a functional shop management solution using only Python fundamentals.  
- Provide a realistic simulation of small retail shop operations.  
- Help beginners apply programming concepts to a real-life use case.  
- Maintain clean project structure with documentation, explanations, and testability.  

# Features:

1. Add New Product
- Enter name, price, stock units, category  
- Prevents duplicate product names  
- Automatically stores data in inventory dictionary  

2. View Product List 
- Shows all available products  
- Displays price, stock quantity, and category  
- Helps during billing and restocking  

3. Search Products
- Search by name   
- Useful for customer queries  

4. Billing System 
- Add multiple items to a customer bill  
- Reduces stock quantity automatically  
- Calculates 18% GST  
- Shows total, GST amount, and final payable amount  
- Prevents billing if stock is insufficient  

5. Update Product Stock
- Add new stock to existing items  
- Update prices  
- Used for daily shop restocking  

6. Delete Products
- Remove discontinued items  
- Prevents accidental removal using confirmation  

7. Automatic Error Handling
- Handles wrong inputs    
- Ensures menu continues running smoothly  


# Technologies/Tools Used:

- Language: Python 3.x
- Development Environment: standard IDE (VS Code).
- Libraries/Modules: Pure Python Standard Library.

# Steps to Install & Run the Project:

Since this is a single, self-contained Python script, installation is straightforward.

1.  Clone or Download: Save the code into a file named `main.py`.
2.  Open Terminal/Command Prompt: Navigate to the directory where you saved `main.py`.
3.  Run the Script: Execute the file using the Python interpreter:

    ```bash
    python main.py
    ```

4.  Follow On-Screen Prompts: The system will guide you through choosing your role (Owner or Customer).

# Instructions for Testing:

To thoroughly test the system, follow the steps below in your terminal session:

# Test Case 1: Owner Inventory Management

1.  Start the script and choose **1. Owner**.
2.  Enter the password: **`1234`**.
3.  Test Product Addition (Choice 1): Add a new item, e.g., "Sharpener" (Price: 5.0, Quantity: 50).
4.  Test Stock Update (Choice 2 - Regular Update): Update "Pen" by adding **10** quantity.
5.  Test Low Stock Alert (Choice 2 - Trigger Alert): Update "Notebook" by adding **1** quantity (The original quantity was 8, if a sale reduces it below 5, the alert will fire). *Note: The low stock alert in the Owner section is triggered if the resulting stock is $\le 5$ AFTER the update.*
6.  Test View Inventory (Choice 3):**Verify that "Sharpener" is listed and the quantities for "Pen" and "Notebook" are updated.**
7.  Choose **4. Exit Owner Panel**.

# Test Case 2: Customer Billing and Stock Check

1.  **Start the script** (or continue from the Owner exit).
2.  The script moves automatically to the **Customer Billing Section**.
3.  **Test Successful Purchase:** Buy **5** x "Pen".
4.  **Test Low Stock Alert on Sale:** Buy **3** x "Notebook" (This should leave 6 - 3 = 3 units, triggering the low stock alert).
5.  **Test Stock Failure:** Attempt to buy **200** x "Pencil" (This should result in the "Not enough stock!" message).
6.  Enter **`no`** when prompted for "Anything else?".
7.  **Review the Bill:** Verify that the **18% GST** and **10% Discount** calculations are correct on the final bill.
8.  **Review the Sales Report:** Ensure only the successful transactions for "Pen" and "Notebook" are logged.

<img width="623" height="573" alt="Screenshot 2025-11-23 at 8 14 10 PM" src="https://github.com/user-attachments/assets/d4a807f8-dca4-4d34-a0b7-f18baa9098c2" />

<img width="626" height="579" alt="Screenshot 2025-11-23 at 8 14 37 PM" src="https://github.com/user-attachments/assets/90c42751-3dd8-4a3b-8160-433c73f30af7" />


<img width="842" height="614" alt="Screenshot 2025-11-23 at 8 18 21 PM" src="https://github.com/user-attachments/assets/091529a0-d242-4d53-85f1-ef39bcecff3e" />
