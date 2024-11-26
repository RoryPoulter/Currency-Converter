# Currency-Converter

Webpage for converting between currencies. Uses a Flask backend and uses an API to fetch current conversion rates.

## Installation
### Manual Installation
* Install the dependencies:
```bash 
pip install -r path/tp/requirements.txt
```
* Get an API key from [here](https://exchangeratesapi.io/)
  * The free key allows up to 100 requests per month
* Create `.env` file and store API key:
```bash
echo "ER_API_KEY=<your key here>" >> .env
```


## Usage
* Run the file `server.py`
* Open your browser and type `127.0.0.1:5000` in the address bar
* Enter the amount to convert, the original currency, and the currency to be converted to
* Press `Convert`