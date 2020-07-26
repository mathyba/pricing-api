"""Pricing API

Provides instrument pricing via the Yahoo Finance API"""

import requests
from flask import Flask, request, jsonify


app = Flask(__name__)

URL = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
headers = {
    "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    # This is an example key. Replace with your own.
    "x-rapidapi-key": "e5c223a73cmsh2d95886314eea2fp11e5e3jsn809a40a625e6",
}


@app.route("/", methods=["GET"])
def get_price():
    """Provide current pricing information by querying the Yahoo Finance API"""
    try:
        symbol = request.args.get("symbol")
        if symbol is None:
            msg = 'The URL must include a symbol parameter: "https://localhost:5000/?symbol=CAT""'
            return jsonify({"message": msg})
        ret = requests.request("GET", URL, headers=headers, params={"symbol": symbol})
        if not any(ret):
            return jsonify({})
        return jsonify(
            {
                "symbol": symbol.upper(),
                "price": ret.json().get("price").get("regularMarketPrice").get("raw"),
                "currency": ret.json().get("price").get("currencySymbol"),
            }
        )
    except Exception as err:
        return jsonify({"message": "An unknown error occured: {}".format(err)})


if __name__ == "__main__":
    # Run on 0.0.0.0 rather than localhost for access from outside the Docker container
    app.run(debug=True, host="0.0.0.0")
