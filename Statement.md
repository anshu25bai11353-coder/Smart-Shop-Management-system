# Project Statement: Smart-Shop-Management-system

# 1. Problem Statement

Small retail businesses, kiosks, and stationery shops often struggle with **manual inventory tracking** and **inaccurate billing**. These manual processes lead to several issues:

1.  **Stockouts:** Failing to identify low-stock items in time, resulting in lost sales.
2.  **Billing Errors:** Mistakes in price calculation, especially when including taxes (like GST) and discounts.
3.  **Inefficient Record Keeping:** Difficulty in tracking daily sales and revenue accurately without digital logging.

The current system lacks a unified, real-time solution for managing inventory levels and generating compliant, error-free customer bills.

---

# 2. Scope of the Project

The project is a **standalone, console-based application** designed to automate the core inventory and sales functions of a small retail business.

# In-Scope:
* Real-time update and display of product inventory and prices.
* Secure, password-protected Owner interface for stock management (add, update).
* Customer interface for transaction processing.
* Automatic calculation of **18% GST** and application of a **10% discount**.
* Generation of a detailed, itemized final bill.
* Recording sales data and generating a basic sales report.
* Implementing **Low Stock Alerts** (when stock $\le 5$) during both owner updates and customer sales.

# Out-of-Scope (Future Enhancements):
* Database integration (currently uses in-memory dictionaries).
* Graphical User Interface (GUI).
* Integration with external hardware (e.g., barcode scanners, receipt printers).
* Advanced financial reporting (e.g., profit/loss statements).
* User authentication for multiple roles beyond a single Owner password.

---

# 3. Target Users

The system is designed for two primary user groups with distinct needs:

| User Role | Primary Needs |
| :--- | :--- |
| **Shop Owner/Manager** | Needs a secure way to manage inventory, monitor stock levels, and ensure product data (price, quantity) is correct. |
| **Sales Clerk/Cashier** | Needs a fast, accurate, and easy-to-use tool to process customer transactions and generate professional bills. |

---

# 4. High-Level Features

| Feature Category | Description |
| :--- | :--- |
| **Inventory Control** | Owners can add new products and update quantities of existing stock. Includes an alert system for critical low stock levels. |
| **Sales Processing** | Allows clerks to select items, specify quantities, and automatically check against available stock before finalizing a sale. |
| **Financial Calculation** | Applies mandatory **18% GST** to all items and a promotional **10% discount** to the total amount before payment. |
| **Reporting & Billing** | Generates a clear, itemized final bill for the customer and logs all successful transactions for a summary sales report. |
