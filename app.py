from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_csv('wallet_scores.csv')
        df.columns = ['wallet_id', 'score'] 
        wallets = df.to_dict(orient='records')
        return render_template('index.html', wallets=wallets)
    except Exception as e:
        return f"Error loading data: {e}"

if __name__ == '__main__':
    app.run(debug=True)
