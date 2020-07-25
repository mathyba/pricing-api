"""Pricing API

Provides instrument pricing via the Yahoo Finance API"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_pricing():
    """Retrieve pricing information"""
    return "Pending pricing info"


if __name__ == "__main__":
    app.run(debug=True)
