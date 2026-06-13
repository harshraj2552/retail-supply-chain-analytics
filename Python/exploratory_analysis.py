import pandas as pd
import matplotlib.pyplot as plt

orders_df = pd.read_csv("data/raw/orders.csv")

print("Dataset Shape:")
print(orders_df.shape)

print("\nFirst 5 Rows:")
print(orders_df.head())
print("\nDataset Information:")
print(orders_df.info())

print("\nMissing Values:")
print(orders_df.isnull().sum())

print("\nStatistical Summary:")
print(orders_df.describe())
plt.figure(figsize=(8,5))
plt.hist(orders_df["sales_amount"], bins=30)

plt.title("Sales Amount Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Number of Orders")

plt.show()
# Monthly Revenue Trend

orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])

monthly_revenue = (
    orders_df
    .groupby(orders_df["order_date"].dt.to_period("M"))["sales_amount"]
    .sum()
)

plt.figure(figsize=(12,5))
monthly_revenue.plot()

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()
# Monthly Revenue Trend

orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])

monthly_revenue = (
    orders_df
    .groupby(orders_df["order_date"].dt.to_period("M"))["sales_amount"]
    .sum()
)

plt.figure(figsize=(12,5))
monthly_revenue.plot()

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()
products_df = pd.read_csv("data/raw/products.csv")

category_revenue = (
    orders_df.merge(
        products_df[["product_id", "category"]],
        on="product_id"
    )
    .groupby("category")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.show()