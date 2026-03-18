import psycopg2
import pandas as pd

def calculate_customer_kpis():
    print("Starting customer KPI calculations...")

    # -------------------------
    # Connect to PostgreSQL Warehouse
    # -------------------------
    conn = psycopg2.connect(
        dbname="shoppulse_db",
        user="postgres",
        password="Vishishta_28",
        host="localhost",
        port="5432"
    )

    # -------------------------
    # Customer-Level KPI Query
    # -------------------------
    # Aggregates transactional data per customer
    query = """
    SELECT
        customer_id,
        COUNT(DISTINCT invoice_no) AS order_count,
        SUM(total_amount) AS total_spent,
        MAX(invoice_date) AS last_purchase
    FROM fact_orders
    GROUP BY customer_id
    """

    customer_kpis = pd.read_sql(query, conn)

    # -------------------------
    # Save KPI Dataset
    # -------------------------
    output_path = "../data/analytics/customer_kpis.csv"
    customer_kpis.to_csv(output_path, index=False)

    conn.close()

    print("Customer KPI dataset created successfully.")
    print("Saved at:", output_path)


if __name__ == "__main__":
    calculate_customer_kpis()
