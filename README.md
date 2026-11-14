# Smart Grocery Store Management System

## Overview
A console-based Python application that helps a local grocery store owner manage products, stock, customer sales and reports. All data is stored in memory using **lists of dictionaries**, and the program keeps running from a menu until the user chooses to exit.

## Features
1. **Add New Product** – enter ID, name, category, price and stock; duplicate IDs are rejected.
2. **View All Products** – readable table of every product.
3. **Search Product** – search by ID or by name (case-insensitive, partial match).
4. **Update Product Stock** – add to the current stock or set a new quantity.
5. **Process Customer Sale** – checks the product exists and stock is sufficient, calculates the total, deducts stock and shows a purchase summary.
6. **View Sales Records** – list of all completed sales.
7. **Generate Store Report** – totals, revenue, low-stock products, highest and lowest priced products.
8. **Exit**

## Data Structures
Products:
```python
{"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20}
```
Sales records:
```python
{"id": 101, "name": "Milk", "quantity": 2, "total": 500}
```

## Python Concepts Used
- Lists and dictionaries (`.append()`, key/value access)
- Custom functions with parameters and `return`
- `while` and `for` loops, `enumerate()`
- `if / elif / else` conditionals
- String methods: `.strip()`, `.title()`, `.lower()`, `.isdigit()`
- Input validation with `try / except`
- f-string formatting for aligned tables

## Custom Functions
| Function | Purpose |
|---|---|
| `get_int`, `get_price`, `get_text` | Validate user input |
| `find_product_by_id` | Find a product dictionary by ID |
| `print_product` | Print details of one product |
| `add_product` | Add a product (no duplicate IDs) |
| `view_products` | Display all products |
| `search_product` | Search by name or ID |
| `update_stock` | Add or set stock |
| `process_sale` | Handle a customer purchase |
| `view_sales` | Display sales records |
| `generate_report` | Show the store report |
| `show_menu`, `main` | Menu and program loop |

## How to Run
Requires Python 3.8 or later.

```bash
python grocery_store_system.py
```

The program starts with three sample products (Milk, Bread, Rice) for demonstration.

## Sample Output

**Processing a sale**
```
Enter your choice: 5

--- Process Customer Sale ---
Enter product ID: 101
Milk - Price: Rs. 250.00, Available: 20
Enter quantity to purchase: 2

----- Purchase Summary -----
Product   : Milk
Quantity  : 2
Unit price: Rs. 250.00
Total     : Rs. 500.00
Remaining stock: 18
```

**Insufficient stock**
```
Enter quantity to purchase: 50
Sale denied. Only 14 unit(s) available.
```

**Store report**
```
========== STORE REPORT ==========
Total products          : 3
Total available stock   : 72
Total sales transactions: 1
Total revenue           : Rs. 500.00

Products with stock below 5:
  Bread (ID 102) - stock: 4

Highest priced: Rice (Rs. 480.00)
Lowest priced : Bread (Rs. 120.00)
==================================
```

## Notes
- Data is not saved to a file, so it resets when the program closes.
- Invalid inputs (letters instead of numbers, negative values, empty text, duplicate IDs) are rejected and the user is asked again.

## Author
Waleed Shehbaz
