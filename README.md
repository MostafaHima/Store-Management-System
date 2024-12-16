# Store Management System

## Overview
This is a simple Python-based store management system that allows users to manage products in a store. The system includes features to add new products, update existing products, view all products, and manage sales. It also includes functions to check inventory levels and identify products that are low in stock.

## Features
- **Display All Products**: View a list of all products in the store.
- **Search for a Product**: Search for a product by its name or product ID.
- **Add a New Product**: Add a new product to the store's inventory.
- **Update Product Details**: Update the name, category, price, and stock quantity of a product.
- **Stock Quantity Analysis**: Display the stock quantity of all products in the store.
- **Low Inventory**: Identify products with low stock (less than 50 units).
- **Sales Management**: Record a sale by reducing the stock quantity of a product.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/store-management-system.git
   ```
2. Install the required libraries:
  ```bash
pip install prettytable
  ```
### Usage
Run the Python script:
  ```bash
  python main.py
  ```
When prompted, enter your username and password to log in.

Choose one of the following options to interact with the system:

- 1: Show All Products
- 2: Search for a Product
- 3: Add a New Product
- 4: Update Product
- 5: Display Stock Quantity
- 6: Low Inventory
- 7: Add Sales
- 8: Exit


### File Structure
  ```bash
    store-management-system/
  │
  ├── store_management.py      # Main script with the functionality
  ├── products.json            # JSON file to store product data
  ├── README.md                # Project documentation
  └── requirements.txt         # Python package requirements
   ```


  
