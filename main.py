import csv
import os
import time
import requests
import pandas as pd
from utils.data_collection import load_wallets, fetch_wallet_data

ETHERSCAN_API_KEY = "YOUR_API_KEY"
WALLET_FILE = "data/wallets.csv"
DATA_FILE = "wallet_data.csv"
SCORE_FILE = "scores/wallet_scores.csv"

wallets = load_wallets(WALLET_FILE)
fetch_wallet_data(wallets, ETHERSCAN_API_KEY, DATA_FILE)

df = pd.read_csv(DATA_FILE)

def score_wallet(row):
    score = (row['txn_count'] * 0.6 + row['balance'] * 0.4) * 10
    return round(min(score, 1000), 2)

df['risk_score'] = df.apply(score_wallet, axis=1)

os.makedirs("scores", exist_ok=True)
df[['wallet_address', 'risk_score']].to_csv(SCORE_FILE, index=False)

print(f"Wallet scoring complete. Output saved to {SCORE_FILE}")
