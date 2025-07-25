import pandas as pd
from data_preparation import load_wallets
from scoring import score_wallet

wallets = load_wallets("wallets.csv")

scores = [score_wallet(wallet) for wallet in wallets]

scores_df = pd.DataFrame(list(zip(wallets, scores)), columns=["wallet_id", "score"])
scores_df.to_csv("wallet_scores.csv", index=False)

print(" Wallet risk scoring complete. Output saved to wallet_scores.csv")
