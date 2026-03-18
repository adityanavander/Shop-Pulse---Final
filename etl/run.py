from extract import extract
from transform import transform
from load import load

def run_pipeline():
    print("Starting ETL Pipeline...")

    try:
        # -------------------------
        # Step 1: Extract
        # -------------------------
        extract()

        # -------------------------
        # Step 2: Transform
        # -------------------------
        transform()

        # -------------------------
        # Step 3: Load
        # -------------------------
        load()

        print("ETL Pipeline completed successfully.")

    except Exception as e:
        print("ETL Pipeline failed:", e)


if __name__ == "__main__":
    run_pipeline()
