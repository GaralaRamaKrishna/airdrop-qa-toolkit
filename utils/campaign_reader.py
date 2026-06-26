import pandas as pd


def get_campaigns():
    """
    Read the list of campaign URLs from campaigns.csv.

    Each row has a name and a URL.
    Returns them as a list of pairs, like:
    [("Bitget Wallet", "https://web3.bitget.com"), ...]

    To check different campaigns, just edit campaigns.csv.
    """

    df = pd.read_csv("campaigns.csv")

    return list(zip(df["name"], df["url"]))