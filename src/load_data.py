import pandas as pd
from pathlib import Path

RAW       = Path(__file__).parent.parent / "data" / "raw"
PROCESSED = Path(__file__).parent.parent / "data" / "processed"


def load_raw() -> dict[str, pd.DataFrame]:
    files = {
        "orders":       "olist_orders_dataset.csv",
        "items":        "olist_order_items_dataset.csv",
        "payments":     "olist_order_payments_dataset.csv",
        "reviews":      "olist_order_reviews_dataset.csv",
        "customers":    "olist_customers_dataset.csv",
        "products":     "olist_products_dataset.csv",
        "sellers":      "olist_sellers_dataset.csv",
        "geo":          "olist_geolocation_dataset.csv",
        "category_map": "product_category_name_translation.csv",
    }
    date_cols = {
        "orders": [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ]
    }
    dfs = {}
    for key, fname in files.items():
        path = RAW / fname
        if not path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {path}\n"
                "Execute: python src/download_data.py"
            )
        dfs[key] = pd.read_csv(path, parse_dates=date_cols.get(key, False))
    return dfs


def build_master(dfs: dict) -> pd.DataFrame:
    pay_agg = (
        dfs["payments"]
        .groupby("order_id")
        .agg(
            payment_value=("payment_value", "sum"),
            payment_type=("payment_type", "first"),
            installments=("payment_installments", "max"),
        )
        .reset_index()
    )

    rv_dedup = (
        dfs["reviews"]
        .sort_values("review_score", ascending=False)
        .drop_duplicates("order_id")[["order_id", "review_score"]]
    )

    df = (
        dfs["orders"]
        .merge(dfs["items"],     on="order_id",    how="inner")
        .merge(pay_agg,          on="order_id",    how="left")
        .merge(dfs["customers"], on="customer_id", how="left")
        .merge(dfs["products"],  on="product_id",  how="left")
        .merge(dfs["category_map"], on="product_category_name", how="left")
        .merge(rv_dedup,         on="order_id",    how="left")
    )

    df = df[df["order_status"] == "delivered"].copy()

    df["delivery_days"]  = (df["order_delivered_customer_date"] - df["order_purchase_timestamp"]).dt.days
    df["estimated_days"] = (df["order_estimated_delivery_date"] - df["order_purchase_timestamp"]).dt.days
    df["delay_days"]     = df["delivery_days"] - df["estimated_days"]
    df["is_late"]        = df["delay_days"] > 0

    df["year"]        = df["order_purchase_timestamp"].dt.year
    df["month"]       = df["order_purchase_timestamp"].dt.month
    df["hour"]        = df["order_purchase_timestamp"].dt.hour
    df["day_of_week"] = df["order_purchase_timestamp"].dt.day_name()
    df["year_month"]  = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

    df["category_en"] = df["product_category_name_english"].fillna(
        df["product_category_name"].str.replace("_", " ")
    )

    return df.dropna(subset=["delivery_days"])


def load_geo(dfs: dict) -> pd.DataFrame:
    return dfs["geo"].drop_duplicates("geolocation_zip_code_prefix")
