"""Server for hosting webpage
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form():
    """Loads the webpage

    Returns:
        _type_: The content of the webpage
    """
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)
