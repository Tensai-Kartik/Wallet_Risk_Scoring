import requests
import time

ETHERSCAN_API_KEY = "YOUR_API_KEY"

def score_wallet(wallet_id):
    try:
        url = (
            f"https://api.etherscan.io/api"
            f"?module=account&action=txlist"
            f"&address={wallet_id}"
            f"&startblock=0&endblock=99999999"
            f"&sort=asc"
            f"&apikey={ETHERSCAN_API_KEY}"
        )

        response = requests.get(url)
        data = response.json()

        time.sleep(0.25)  

        if data["status"] != "1" or "result" not in data:
            return 0.0

        tx_count = len(data["result"])
        score = min(tx_count * 10, 1000)  

        return round(score, 2)

    except Exception as e:
        print(f"Error scoring {wallet_id}: {e}")
        return 0.0
