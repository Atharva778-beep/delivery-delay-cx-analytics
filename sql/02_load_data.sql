USE ecommerce_analytics;

-- 1. Load customers
LOAD DATA INFILE 'C:/Users/Atharva/delivery_delay_cx_analytics/data/raw/olist_customers_dataset.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- 2. Load orders  
LOAD DATA INFILE 'C:/Users/Atharva/delivery_delay_cx_analytics/data/raw/olist_orders_dataset.csv'
INTO TABLE orders
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date);

-- 3. Load order_items
LOAD DATA INFILE 'C:/Users/Atharva/delivery_delay_cx_analytics/data/raw/olist_order_items_dataset.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- 4. Load products
LOAD DATA INFILE 'C:/Users/Atharva/delivery_delay_cx_analytics/data/raw/olist_products_dataset.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- 5. Load order payments
LOAD DATA INFILE 'C:/Users/Atharva/delivery_delay_cx_analytics/data/raw/olist_order_payments_dataset.csv'
INTO TABLE order_payments
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;