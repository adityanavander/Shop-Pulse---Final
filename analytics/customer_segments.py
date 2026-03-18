import pandas as pd

def create_customer_segments():
    print("Creating customer segments...")

    df = pd.read_csv("../data/analytics/churn_predictions.csv")

    # Value segment
    df["value_segment"] = df["monetary"].apply(
        lambda m: "High" if m > 1000 else "Medium" if m > 300 else "Low"
    )

    # Churn flag
    df["at_risk"] = df["churn_probability"] > 0.7

    output_path = "../data/analytics/customer_segments.csv"
    df.to_csv(output_path, index=False)

    print("Customer segments saved at:", output_path)

if __name__ == "__main__":
    create_customer_segments()