import psycopg2
import os

def load():
    print("Starting load process...")

    conn = psycopg2.connect(
        dbname="shoppulse_db",
        user="postgres",
        password="Vishishta_28",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    try:
        # -------------------------
        # Optional: Clear Tables (Full Load Mode)
        # -------------------------
        cur.execute("""
            TRUNCATE dim_customers,
                     dim_products,
                     dim_deals,
                     fact_orders,
                     fact_returns;
        """)

        # -------------------------
        # Load Dimension: Customers
        # -------------------------
        with open("../data/staging/customers.csv", "r") as f:
            cur.copy_expert("""
                COPY dim_customers(customer_id, country)
                FROM STDIN WITH CSV HEADER
            """, f)
        print("Customers loaded.")

        # -------------------------
        # Load Dimension: Products
        # -------------------------
        with open("../data/staging/products.csv", "r") as f:
            cur.copy_expert("""
                COPY dim_products(stock_code, description)
                FROM STDIN WITH CSV HEADER
            """, f)
        print("Products loaded.")

        # -------------------------
        # Load Dimension: Deals
        # -------------------------
        deals_path = "../data/staging/deals.csv"

        if os.path.exists(deals_path):
            with open(deals_path, "r") as f:
                cur.copy_expert("""
                    COPY dim_deals(
                        deal_id,
                        stock_code,
                        discount_percent,
                        start_date,
                        end_date,
                        deal_type
                    )
                    FROM STDIN WITH CSV HEADER
                """, f)
            print("Deals loaded.")
        else:
            print("No deals file found. Skipping deals.")

        # -------------------------
        # Load Fact: Orders (Sales)
        # -------------------------
        with open("../data/staging/orders.csv", "r") as f:
            cur.copy_expert("""
                COPY fact_orders(
                    invoice_no,
                    stock_code,
                    customer_id,
                    quantity,
                    unit_price,
                    invoice_date,
                    total_amount
                )
                FROM STDIN WITH CSV HEADER
            """, f)
        print("Orders loaded.")

        # -------------------------
        # Load Fact: Returns
        # -------------------------
        with open("../data/staging/returns.csv", "r") as f:
            cur.copy_expert("""
                COPY fact_returns(
                    invoice_no,
                    stock_code,
                    customer_id,
                    quantity,
                    unit_price,
                    return_date,
                    return_amount
                )
                FROM STDIN WITH CSV HEADER
            """, f)
        print("Returns loaded.")

        conn.commit()
        print("Load completed successfully.")

    except Exception as e:
        conn.rollback()
        print("Error during load:", e)

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    load()
