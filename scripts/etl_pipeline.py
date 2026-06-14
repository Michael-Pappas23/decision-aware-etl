import pandas as pd

def run_etl():

    sales_df = pd.read_csv("data/sales.csv")
    inventory_df = pd.read_csv("data/inventory.csv")

    merged_df = pd.merge(
        sales_df,
        inventory_df,
        on=["Date", "Product"]
    )

    return merged_df