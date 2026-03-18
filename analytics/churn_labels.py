import pandas as pd

def create_churn_labels():
    print("Generating churn labels...")

    # -------------------------
    # Load RFM features
    # -------------------------
    df = pd.read_csv("../data/analytics/rfm_features.csv")

    # -------------------------
    # Define churn rule
    # -------------------------
    # Customer inactive > 90 days → churn
    df["churn"] = (df["recency_days"] > 90).astype(int)

    # Save churn dataset
    output_path = "../data/analytics/churn_dataset.csv"
    df.to_csv(output_path, index=False)

    print("Churn dataset created at:", output_path)


if __name__ == "__main__":
    create_churn_labels()
