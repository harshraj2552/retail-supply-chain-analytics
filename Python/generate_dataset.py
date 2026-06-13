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