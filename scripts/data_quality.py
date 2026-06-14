def check_missing_values(df):
    return df.isnull().sum().sum()


def check_negative_inventory(df):
    return df[df["Stock_Level"] < 0]