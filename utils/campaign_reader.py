import pandas as pd


def get_campaigns():
    df = pd.read_csv("campaigns.csv")

    return list(zip(df["name"], df["url"]))