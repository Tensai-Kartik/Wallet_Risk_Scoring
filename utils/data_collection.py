import os
import time
import requests
import pandas as pd

def load_wallets(wallet_file):
    df = pd.read_csv(wallet_file)
    if 'wallet_address' not in df.columns:
        raise ValueError(f"'wallet_address' column not found. Found: {df.columns.tolist()}")
    return df['wallet_address'].tolist()

def fetch_wallet_data(wallets, api_key, output_file="wallet_data.csv"):
    if os.path.exists(output_file):
        existing_df = pd.read_csv(output_file)
        processed_wallets = set(existing_df['wallet_address'].str.lower())
    else:
        existing_df = pd.DataFrame(columns=['wallet_address', 'balance', 'txn_count'])
        processed_wallets = set()

    new_data = []

    for i, wallet in enumerate(wallets):
        wallet_lower = wallet.lower()
        if wallet_lower in processed_wallets:
            continue

        for attempt in range(3):
            try:
                balance_url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet}&tag=latest&apikey={api_key}"
                balance_res = requests.get(balance_url, timeout=10)
                balance_res.raise_for_status()
                balance = int(balance_res.json()['result']) / 1e18

                txn_url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionCount&address={wallet}&tag=latest&apikey={api_key}"
                txn_res = requests.get(txn_url, timeout=10)
                txn_res.raise_for_status()
                txn_count = int(txn_res.json()['result'], 16)

                new_data.append({
                    'wallet_address': wallet,
                    'balance': balance,
                    'txn_count': txn_count
                })
                break
            except Exception:
                time.sleep(1)
        else:
            continue

        if len(new_data) % 5 == 0 or i == len(wallets) - 1:
            temp_df = pd.DataFrame(new_data)
            combined_df = pd.concat([df for df in [existing_df, temp_df] if not df.empty], ignore_index=True)
            combined_df.to_csv(output_file, index=False)
            new_data.clear()
            existing_df = combined_df

        time.sleep(0.5)
