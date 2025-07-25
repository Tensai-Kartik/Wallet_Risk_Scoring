import pandas as pd

def load_wallets(csv_path="wallets.csv"):
    df = pd.read_csv(csv_path)
    if "wallet_id" not in df.columns:
        raise ValueError("CSV must contain a column named 'wallet_id'")
    return df["wallet_id"].tolist()
