import pandas as pd
import os

def transform():
    print("Starting transformation process...")

    staging_input_path = "../data/staging/online_retail_extracted.csv"


    if not os.path.exists(staging_input_path):
        raise FileNotFoundError("Extracted file not found. Run extract.py first.")

    df = pd.read_csv(staging_input_path)

    # -------------------------
    # Basic Cleaning
    # -------------------------
    df = df.dropna(subset=['CustomerID'])
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int)

    # -------------------------
    # Separate SALES and RETURNS
    # -------------------------
    sales_df = df[df['Quantity'] > 0].copy()
    returns_df = df[df['Quantity'] < 0].copy()

    # -------------------------
    # Dimension: Customers
    # -------------------------
    customers = df[['CustomerID', 'Country']].drop_duplicates()
    customers.to_csv('../data/staging/customers.csv', index=False)

    # -------------------------
    # Dimension: Products
    # -------------------------
    products = df[['StockCode', 'Description']].drop_duplicates()
    products.to_csv('../data/staging/products.csv', index=False)

    # -------------------------
    # Fact: Orders (Sales)
    # -------------------------
    sales_df['TotalAmount'] = sales_df['Quantity'] * sales_df['UnitPrice']

    orders = sales_df[['InvoiceNo', 'StockCode', 'CustomerID',
                       'Quantity', 'UnitPrice', 'InvoiceDate', 'TotalAmount']]

    orders.to_csv('../data/staging/orders.csv', index=False)

    # -------------------------
    # Fact: Returns
    # -------------------------
    returns_df['Quantity'] = returns_df['Quantity'].abs()
    returns_df['ReturnAmount'] = returns_df['Quantity'] * returns_df['UnitPrice']

    returns = returns_df[['InvoiceNo', 'StockCode', 'CustomerID',
                          'Quantity', 'UnitPrice', 'InvoiceDate', 'ReturnAmount']]

    returns.to_csv('../data/staging/returns.csv', index=False)

    # -------------------------
    # Dimension: Deals (manual dataset)
    # -------------------------
    deals_raw_path = "../data/raw/deals.csv"

    if os.path.exists(deals_raw_path):
        deals = pd.read_csv(deals_raw_path)
        deals.to_csv('../data/staging/deals.csv', index=False)
        print("Deals staged successfully.")
    else:
        print("No deals file found. Skipping deals staging.")

    print("Transformation completed successfully.")

if __name__ == "__main__":
    transform()
