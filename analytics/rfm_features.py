import pandas as pd

def create_rfm_features():
    print("Creating RFM features...")

    # -------------------------
    # Load customer KPIs
    # -------------------------
    df = pd.read_csv("../data/analytics/customer_kpis.csv")

    # Convert last_purchase to datetime
    df["last_purchase"] = pd.to_datetime(df["last_purchase"])

    # Reference date = most recent purchase in dataset
    reference_date = df["last_purchase"].max()

    # -------------------------
    # RFM Calculations
    # -------------------------
    df["recency_days"] = (reference_date - df["last_purchase"]).dt.days
    df["frequency"] = df["order_count"]
    df["monetary"] = df["total_spent"]

    # Select RFM columns
    rfm = df[["customer_id", "recency_days", "frequency", "monetary"]]

    # Save
    output_path = "../data/analytics/rfm_features.csv"
    rfm.to_csv(output_path, index=False)

    print("RFM dataset created at:", output_path)


if __name__ == "__main__":
    create_rfm_features()
