# Wallet Risk Scoring (Aave V2)
A simple Flask web app that scores Ethereum wallets for risk and displays the results in a web dashboard.

##  Data Collection
The wallet list is provided via a CSV file (`wallets.csv`). For each wallet, we simulate fetching:
- Total Borrowed
- Total Collateral
- Liquidation Events
- Health Factor

##  Feature Selection
Key features used for scoring:
- **Utilization Ratio** = Borrowed / Collateral
- **Liquidations** = Binary flag for risk
- **Health Factor** = Critical metric from Aave

##  Scoring Method
- Score starts from 1000
- Penalized for high utilization, low health factor, and liquidation history
- Output range: 0–1000

##  Bonus Enhancements
- Modular structure (preprocessing, scoring, main logic)
- Easily replace simulated data with Aave subgraph API data
- Extensible for additional indicators (asset volatility, wallet age, etc.)

##  Deliverables
- `wallet_scores.csv` — contains risk scores for all provided wallets
- `README.md` — explanation of methodology

##  How to Run

1. Clone this repo or download it
2. Install Python dependencies:

```bash
pip install -r requirements.txt
python app.py