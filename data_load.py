import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:atharva$123778@localhost:3306/delivery_delay_cx_analytics"
)

files = {
    "customers": "data/raw/olist_customers_dataset.csv",
    "geolocation": "data/raw/olist_geolocation_dataset.csv",
    "order_items": "data/raw/olist_order_items_dataset.csv",
    "order_payments": "data/raw/olist_order_payments_dataset.csv",
    "order_reviews": "data/raw/olist_order_reviews_dataset.csv",
    "orders": "data/raw/olist_orders_dataset.csv",
    "products": "data/raw/olist_products_dataset.csv",
    "sellers": "data/raw/olist_sellers_dataset.csv",
    "product_category_name_translation": "data/raw/product_category_name_translation.csv"
}

for table_name, file_path in files.items():
    print(f"Loading {table_name} from {file_path} ...")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    print(f"Loaded {table_name}: {len(df)} rows")

print("All CSV files loaded successfully!")