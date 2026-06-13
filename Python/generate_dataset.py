import pandas as pd
import numpy as np
from faker import Faker
import random
import random

fake = Faker()
# Create suppliers data
suppliers = []

for i in range(1, 21):
    suppliers.append({
        "supplier_id": f"S{i:03d}",
        "supplier_name": fake.company(),
        "supplier_location": fake.city(),
        "average_delivery_days": random.randint(2, 12),
        "supplier_rating": round(random.uniform(3.0, 5.0), 1)
    })

suppliers_df = pd.DataFrame(suppliers)

print(suppliers_df.head())
suppliers_df.to_csv("Data/raw/suppliers.csv", index=False)

print("Suppliers dataset saved successfully!")
print(suppliers_df.shape)
print(suppliers_df["supplier_id"].tolist())
# Create products data
categories = {
    "Electronics": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Furniture": ["Chair", "Table", "Desk", "Bookshelf", "Cabinet"],
    "Office Supplies": ["Notebook", "Pen", "Folder", "Stapler", "Paper"],
    "Home Appliances": ["Mixer", "Toaster", "Kettle", "Iron", "Fan"]
}

products = []

for i in range(1, 501):
    category = random.choice(list(categories.keys()))
    product_type = random.choice(categories[category])
    cost_price = random.randint(200, 5000)
    selling_price = round(cost_price * random.uniform(1.2, 1.8), 2)

    products.append({
        "product_id": f"P{i:04d}",
        "product_name": f"{fake.word().title()} {product_type}",
        "category": category,
        "cost_price": cost_price,
        "selling_price": selling_price,
        "supplier_id": random.choice(suppliers_df["supplier_id"].tolist())
    })

products_df = pd.DataFrame(products)

print(products_df.head())
print(products_df.shape)

products_df.to_csv("data/raw/products.csv", index=False)

print("Products dataset saved successfully!")
# Create warehouses data
warehouses = [
    {
        "warehouse_id": "W001",
        "warehouse_name": "North Distribution Center",
        "city": "Delhi",
        "state": "Delhi",
        "capacity": 50000
    },
    {
        "warehouse_id": "W002",
        "warehouse_name": "West Fulfillment Hub",
        "city": "Mumbai",
        "state": "Maharashtra",
        "capacity": 65000
    },
    {
        "warehouse_id": "W003",
        "warehouse_name": "South Storage Unit",
        "city": "Bengaluru",
        "state": "Karnataka",
        "capacity": 55000
    },
    {
        "warehouse_id": "W004",
        "warehouse_name": "East Logistics Center",
        "city": "Kolkata",
        "state": "West Bengal",
        "capacity": 45000
    },
    {
        "warehouse_id": "W005",
        "warehouse_name": "Central Supply Hub",
        "city": "Nagpur",
        "state": "Maharashtra",
        "capacity": 40000
    }
]

warehouses_df = pd.DataFrame(warehouses)

print(warehouses_df)
print(warehouses_df.shape)

warehouses_df.to_csv("data/raw/warehouses.csv", index=False)

print("Warehouses dataset saved successfully!")