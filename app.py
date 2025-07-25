from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

SCORES_FILE = 'scores/wallet_scores.csv'

def read_scores():
    scores = []
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                wallet = row.get('wallet_address')
                score = row.get('risk_score')
                if wallet and score:
                    try:
                        scores.append((wallet, int(float(score))))
                    except ValueError:
                        continue
    return scores

@app.route('/')
def index():
    scores = read_scores()
    return render_template('index.html', scores=scores)

@app.route('/scores')
def get_scores_html():
    scores = read_scores()
    html_rows = ""
    for wallet, score in scores:
        css_class = (
            "score-low" if score >= 75 else
            "score-medium" if score >= 40 else
            "score-high"
        )
        html_rows += f"<tr><td>{wallet}</td><td class='{css_class}'>{score}</td></tr>"
    return html_rows

if __name__ == '__main__':
    app.run(debug=True)
