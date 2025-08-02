# Wallet Risk Scoring Dashboard
This project scores Ethereum wallet addresses based on their balance and transaction count, assigning a risk score between 0 and 1000, and displays the results on a web dashboard.

# Data Collection
The wallet list is provided via a CSV file (data/wallets.csv) containing:
wallet_address
0x742d35Cc6634C0532925a3b844Bc454e4438f44e
0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0
...
For each wallet, we fetch:
ETH Balance
Total Transaction Count
Using the Etherscan API.

Feature Selection
Key features used for risk scoring:
Transaction Count: Indicates wallet activity
ETH Balance: Measures financial strength

# Scoring Method
Base score calculated as:
score = (txn_count * 0.6 + balance_in_eth * 0.4)
Then scaled linearly to fit 0–1000 range
Higher score = lower risk

# Deliverables
data/wallets.csv — input list of wallet addresses
wallet_data.csv — intermediate fetched data (auto-created)
scores/wallet_scores.csv — final output with scores
templates/index.html — interactive dashboard UI
app.py — Flask app backend
main.py — core data pipeline
utils/data_collection.py — helper logic for API and scoring
README.md — documentation

# How to Run
1)Clone this repository or download the code.
2)Install required Python libraries:
pip install flask pandas requests
3)Open main.py and paste your Etherscan API key:
ETHERSCAN_API_KEY = "YOUR_API_KEY"
4)Add your wallet addresses in data/wallets.csv 
5)Run the scoring script:
python main.py
6)Launch the web dashboard:
python app.py
Then open http://127.0.0.1:5000 in your browser.

# Risk Score 
| Range    | Category | Color     |
| -------- | -------- | --------- |
| 0–399    | High     | 🔴 Red    |
| 400–749  | Medium   | 🟡 Yellow |
| 750–1000 | Low      | 🟢 Green  |

## Author
Kartik Sharma
