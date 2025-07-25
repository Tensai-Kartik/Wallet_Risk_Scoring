import hashlib
import random

def score_wallet(wallet_id):
   
    stable_hash = int(hashlib.sha256(wallet_id.encode()).hexdigest(), 16)
    random.seed(stable_hash)
    return round(random.uniform(0, 100), 2)
