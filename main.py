from scripts.generate_data import generate_data
from scripts.etl_pipeline import run_etl
from scripts.data_quality import (
    check_missing_values,
    check_negative_inventory
)
from scripts.risk_scoring import calculate_decision_risk
from scripts.decision_engine import get_stock_status


def main():

    print("Pipeline started")

    # 1. Generate data
    generate_data()

    # 2. ETL
    df = run_etl()

    # 3. Decision feature
    df["Stock_Status"] = df["Stock_Level"].apply(get_stock_status)

    # 4. Data quality
    missing = check_missing_values(df)
    negative = check_negative_inventory(df)

    # 5. Risk score
    risk = calculate_decision_risk(
        missing,
        len(negative)
    )

    # 6. Output
    print(df)
    print("\nMISSING:", missing)
    print("\nNEGATIVE STOCK:", negative)
    print("\nDECISION RISK:", risk)


if __name__ == "__main__":
    main()