import pandas as pd
import os

os.makedirs("data", exist_ok=True)

def generate_data():

    sales_data = [
        ["2026-01-01", "Laptop", 15],
        ["2026-01-01", "Mouse", 31],
        ["2026-01-01", "Keyboard", 8],
        ["2026-01-01", "Monitor", 5],
    ]

    sales_df = pd.DataFrame(sales_data, columns=["Date", "Product", "Units_Sold"])
    sales_df.to_csv("data/sales.csv", index=False)

    inventory_df = sales_df.copy()
    inventory_df["Stock_Level"] = inventory_df["Units_Sold"]
    inventory_df.loc[inventory_df["Product"] == "Monitor", "Stock_Level"] = -5
    inventory_df.drop(columns=["Units_Sold"], inplace=True)

    inventory_df.to_csv("data/inventory.csv", index=False)

    print("DATA GENERATED")

    return sales_df, inventory_df