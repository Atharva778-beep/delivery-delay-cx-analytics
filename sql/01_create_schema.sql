-- E-Commerce Analytics Database
CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

-- Drop tables if exist (clean start)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

-- 1. Customers
CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_state VARCHAR(10),
    customer_city VARCHAR(100)
);

-- 2. Orders (with our calculated features)
CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),
    order_status VARCHAR(20),
    delivery_days INT,
    delay_days INT,
    is_late TINYINT(1),
    delay_bucket VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 3. Reviews
CREATE TABLE reviews (
    order_id VARCHAR(50) PRIMARY KEY,
    avg_review_score DECIMAL(3,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 4. Order Items
CREATE TABLE order_items (
    order_id VARCHAR(50),
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    INDEX idx_order_id (order_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 5. Products
CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    category_english VARCHAR(100)
);