"""Server for hosting webpage
"""

import os
import json
import urllib.request
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


def convert(start_curr: str, final_curr: str, amount: str, dplaces: int = 3) -> str | int:
    """Converts between the two currencies.     
    Error codes:           
    1: Start and final currencies are the same

    Args:
        start_curr (str): The initial currency
        final_curr (str): The final currency
        amount (str): The amount to be converted
        dplaces (int, opitonal): The number of decimal places for the result. Defaults to 3.

    Returns:
        str | int: A string of the converted amount if successful or integer error code if failed.
    """
    if start_curr == final_curr:
        return 1

    dotenv_path = Path("../.env")
    load_dotenv(dotenv_path=dotenv_path)
    er_api_key = os.getenv("ER_API_KEY")
    base_url = "https://api.exchangeratesapi.io/v1/latest?access_key="
    with urllib.request.urlopen(base_url+er_api_key) as url:
        data = json.load(url)
    amount = float(amount)
    result = amount * data["rates"][final_curr] / data["rates"][start_curr]
    return str(round(result, dplaces))


@app.route("/", methods=["GET", "POST"])
def form():
    """Loads the webpage

    Returns:
        _type_: The content of the webpage
    """
    if request.method == "POST":
        start_curr = request.form['start_currency']
        final_curr = request.form['final_currency']
        amount = request.form['amount']
        result = convert(start_curr, final_curr, amount)
        start_to_final = f"1 {start_curr} = {convert(start_curr, final_curr, '1')} {final_curr}"
        final_to_start = f"1 {final_curr} = {convert(final_curr, start_curr, '1')} {start_curr}"
        if isinstance(result, int):
            return jsonify({'error': result})
        return jsonify({'output': result,
                        'start_to_final': start_to_final,
                        'final_to_start': final_to_start})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
