import pandas as pd
import os

def extract():
    print("Starting extraction process...")

    raw_path = "../data/raw/online_retail.csv"
    staging_path = "../data/staging/online_retail_extracted.csv"


    # Check if file exists
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw file not found at {raw_path}")

    # Read raw dataset
    df = pd.read_csv(raw_path)

    # Basic validation
    if df.empty:
        raise ValueError("Extracted dataset is empty")

    print(f"Rows extracted: {len(df)}")
    print("Columns detected:", list(df.columns))

    # Save to staging
    df.to_csv(staging_path, index=False)

    print("Extraction completed. Data moved to staging.")

if __name__ == "__main__":
    extract()
