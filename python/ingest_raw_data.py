import pandas as pd
from sqlalchemy import create_engine

# ----------------------------
# Database connection
# ----------------------------

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "bi_project"
DB_USER = "samarlabidi"
DB_PASSWORD = "101199"


engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ----------------------------
# File paths
# ----------------------------
DATA_PATH = "data/raw/"

files = {
    "raw_orders": "olist_orders_dataset.csv",
    "raw_customers": "olist_customers_dataset.csv",
    "raw_order_items": "olist_order_items_dataset.csv",
}

# ----------------------------
# Ingestion logic
# ----------------------------
for table_name, file_name in files.items():
    print(f"Ingesting {file_name} into {table_name}...")

    df = pd.read_csv(DATA_PATH + file_name)

    print(f"Rows: {len(df)}")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

print("Ingestion completed successfully.")
