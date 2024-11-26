"""Server for hosting webpage
"""

import json
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


def convert(start_curr: str, final_curr: str, amount: str) -> str | int:
    """Converts between the two currencies.     
    Error codes:    
    1: Amount input missing    
    2: String input for amount  
    3: Amount below or equal to zero        
    4: Start and final currencies are the same

    Args:
        start_curr (str): The initial currency
        final_curr (str): The final currency
        amount (str): The amount to be converted

    Returns:
        str | int: A string of the converted amount if successful or integer error code if failed.
    """
    if not amount:
        return 1
    try:
        amount = float(amount)
    except ValueError:
        return 2
    if amount <= 0:
        return 3
    if start_curr == final_curr:
        return 4
    with open("test/server-test/static/exchange_rates_test_file.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    result = amount * data["rates"][final_curr] / data["rates"][start_curr]
    return str(result)


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
        if isinstance(result, int):
            ERRORS = {
                1: "Missing amount!",
                2: "Invalid amount: must be a number!",
                3: "Invalid amount: must be greater than 0!",
                4: "Converting to and from same currency!"
                }
            return jsonify({'error': ERRORS[result]})
        return jsonify({'output' : result})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
