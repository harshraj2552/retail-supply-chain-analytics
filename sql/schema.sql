CREATE DATABASE IF NOT EXISTS retail_supply_chain;

USE retail_supply_chain;

CREATE TABLE suppliers (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(100),
    supplier_location VARCHAR(100),
    average_delivery_days INT,
    supplier_rating DECIMAL(2,1)
);

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    cost_price DECIMAL(10,2),
    selling_price DECIMAL(10,2),
    supplier_id VARCHAR(10)
);

CREATE TABLE warehouses (
    warehouse_id VARCHAR(10) PRIMARY KEY,
    warehouse_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    capacity INT
);

CREATE TABLE inventory (
    inventory_id VARCHAR(10) PRIMARY KEY,
    product_id VARCHAR(10),
    warehouse_id VARCHAR(10),
    stock_quantity INT,
    reorder_level INT
);

CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    warehouse_id VARCHAR(10),
    quantity INT,
    sales_amount DECIMAL(10,2),
    discount DECIMAL(4,2),
    delivery_days INT
);