USE retail_supply_chain;

-- 1. Overall Business KPIs
SELECT
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(sales_amount), 2) AS total_revenue,
    ROUND(AVG(sales_amount), 2) AS average_order_value
FROM orders;

-- 2. Top 10 Products by Revenue
SELECT
    p.product_name,
    ROUND(SUM(o.sales_amount), 2) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- 3. Monthly Sales Trend
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    ROUND(SUM(sales_amount), 2) AS revenue
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- 4. Revenue by Category
SELECT
    p.category,
    ROUND(SUM(o.sales_amount), 2) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 5. Top Warehouses by Revenue
SELECT
    w.warehouse_name,
    ROUND(SUM(o.sales_amount), 2) AS revenue
FROM orders o
JOIN warehouses w
ON o.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name
ORDER BY revenue DESC;

-- 6. Low Stock Products
SELECT
    i.inventory_id,
    p.product_name,
    w.warehouse_name,
    i.stock_quantity,
    i.reorder_level
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
JOIN warehouses w
ON i.warehouse_id = w.warehouse_id
WHERE i.stock_quantity < i.reorder_level;

-- 7. Top Suppliers by Product Count
SELECT
    s.supplier_name,
    COUNT(p.product_id) AS total_products
FROM suppliers s
JOIN products p
ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_name
ORDER BY total_products DESC
LIMIT 10;

-- 8. Average Delivery Days by Supplier
SELECT
    s.supplier_name,
    s.average_delivery_days,
    s.supplier_rating
FROM suppliers s
ORDER BY s.average_delivery_days ASC;

-- 9. Inventory Value
SELECT
    ROUND(SUM(i.stock_quantity * p.cost_price), 2) AS inventory_value
FROM inventory i
JOIN products p
ON i.product_id = p.product_id;

-- 10. Revenue by Supplier
SELECT
    s.supplier_name,
    ROUND(SUM(o.sales_amount), 2) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
JOIN suppliers s
ON p.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY revenue DESC
LIMIT 10;