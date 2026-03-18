-- ============================
-- ShopPulse Data Warehouse Schema
-- ============================

-- ----------------------------
-- Dimension: Customers
-- ----------------------------
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INT PRIMARY KEY,
    country VARCHAR
);

-- ----------------------------
-- Dimension: Products
-- ----------------------------
CREATE TABLE IF NOT EXISTS dim_products (
    stock_code VARCHAR PRIMARY KEY,
    description TEXT
);

-- ----------------------------
-- Dimension: Deals
-- ----------------------------
CREATE TABLE IF NOT EXISTS dim_deals (
    deal_id VARCHAR PRIMARY KEY,
    stock_code VARCHAR,
    discount_percent NUMERIC,
    start_date DATE,
    end_date DATE,
    deal_type VARCHAR
);

-- ----------------------------
-- Fact: Orders
-- ----------------------------
CREATE TABLE IF NOT EXISTS fact_orders (
    invoice_no VARCHAR,
    stock_code VARCHAR,
    customer_id INT,
    quantity INT,
    unit_price NUMERIC,
    invoice_date TIMESTAMP,
    total_amount NUMERIC,
    PRIMARY KEY (invoice_no, stock_code)
);

-- ----------------------------
-- Fact: Returns
-- ----------------------------
CREATE TABLE IF NOT EXISTS fact_returns (
    invoice_no VARCHAR,
    stock_code VARCHAR,
    customer_id INT,
    quantity INT,
    unit_price NUMERIC,
    return_date TIMESTAMP,
    return_amount NUMERIC,
    PRIMARY KEY (invoice_no, stock_code)
);
