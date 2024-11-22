"""Python file for fetching data from exchange rates API
"""
import os
import json
import urllib.request
from pathlib import Path
from dotenv import load_dotenv


if __name__ == "__main__":
    dotenv_path = Path("../../.env")
    load_dotenv(dotenv_path=dotenv_path)

    ER_API_KEY = os.getenv("ER_API_KEY")
    with urllib.request.urlopen("https://api.exchangeratesapi.io/v1/latest?access_key="+ER_API_KEY) as url:
        data = json.load(url)
        print(data)
