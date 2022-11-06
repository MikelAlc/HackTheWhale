from flask import Flask, render_template
import requests
import pandas as pd


pd.set_option('display.max_rows', 100)

def getOwnership():
    slug = "boredapeyachtclub"
    url = f"https://api.verbwire.com/v1/nft/data/ownershipForSlug?slug={slug}&chain=ethereum&limit=100&page=1&sortDirection=DESC"

    headers = {
        "accept": "application/json",
        "X-API-Key": "sk_live_44463b61-a57b-47a0-a501-bd5ab8c2e71f"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def visualizeOwnership():
    whales = pd.DataFrame(getOwnership()["ownership"]["results"])
    whales = whales[["address", "tokenCount", "floorAskPrice", "onSaleCount", "topBidValue", "totalBidValue", "id"]]


    return whales



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


