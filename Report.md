## Explanation of Methodology

# Data Collection Method
We use the Etherscan API to collect two key metrics for each Ethereum wallet listed in data/wallets.csv:
ETH Balance: Retrieved using the eth_getBalance endpoint, converted from Wei to Ether.
Total Transaction Count: Fetched using the txlist endpoint, representing on-chain activity.
Data is fetched with retries and delays to comply with Etherscan's rate limits and saved in wallet_data.csv for reuse.

# Feature Selection
We chose the following two features due to their public availability, relevance to wallet risk, and lightweight API usage:
| Feature         | Why it was selected                                                                  |
| --------------- | ------------------------------------------------------------------------------------ |
| ETH Balance     | A wallet with a high balance is generally less risky — more "collateralized".        |
| Txn Count       | Active wallets are more likely to be genuine users rather than dormant or malicious. |
These features are simple but meaningful, providing a practical risk estimation in absence of protocol-level metrics (e.g., borrowed/collateral).

# Normalization Method
Because balance and transaction counts are on very different scales, we use min-max normalization:
normalized_txn = (txn_count - min_txn) / (max_txn - min_txn)
normalized_bal = (balance - min_bal) / (max_bal - min_bal)
This brings both values into the range of 0–1, making them comparable and suitable for weighted scoring.

# Scoring Logic
We assign a final risk score using a weighted average of the normalized values:
score = (normalized_txn * 0.6 + normalized_bal * 0.4) * 1000
The score ranges from 0 (high risk) to 1000 (low risk)
60% weight is given to activity (txn count)
40% weight is given to ETH balance
Rounded to the nearest integer, the scores are saved in scores/wallet_scores.csv.

# Justification of Risk Indicators
| Indicator           | Justification                                                                 |
| --------------------|-------------------------------------------------------------------------------|     
| Transaction Count   | Higher activity indicates real, ongoing usage. Inactive wallets may be        |  
|                     | abandoned, dust wallets, or malicious stash accounts.                         |
| ETH Balance Higher  | balance implies better financial backing, similar to collateralization. Empty |
|                     | wallets are often less trustworthy.                                           |
These indicators, while basic, provide a strong starting point for evaluating wallet credibility at scale, with minimal data requirements.

