# Currency-Converter

[![GitHub Release](https://img.shields.io/github/release/RoryPoulter/Currency-Converter.svg?style=flat)]()
![GitHub License](https://img.shields.io/github/license/RoryPoulter/Currency-Converter)
[![GitHub last commit](https://img.shields.io/github/last-commit/RoryPoulter/Currency-Converter.svg?style=flat)]()

Webpage for converting between currencies. Uses a Flask backend and uses an API to fetch current conversion rates.

## Installation
* Get an API key from [here](https://exchangeratesapi.io/)
  * The free key allows up to 100 requests per month
### Manual Installation
* Install the dependencies:
```bash 
pip install -r path/to/requirements.txt
```
* Create `.env` file in the main directory and store API key:
```bash
echo "ER_API_KEY=<your key here>" >> .env
```
* Run the file `server.py`

## Automatic Installation
* Run the file `build.sh`
```bash
cd path/to/.build/
bash build.sh
```

## Usage
* Open your browser and type `127.0.0.1:5000` in the address bar
* Enter the amount to convert, the original currency, and the currency to be converted to
* Press `Convert`
