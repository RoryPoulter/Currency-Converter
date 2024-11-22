"""Python file for converting between currencies and validating inputs 
"""
import json


if __name__ == "__main__":
    with open("test/conversion-test/exchange_rates_test_file.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    CURRENCIES = set(data["rates"].keys())
    print(CURRENCIES)
    curr_1 = input("Enter initial currency: ").upper()
    curr_2 = input("Enter final currency: ").upper()
    amount = float(input("Enter amount to convert: "))

    # Input verification
    if (curr_1 not in CURRENCIES) or (curr_2 not in CURRENCIES):
        raise ValueError("Unknown currency")
    if curr_1 == curr_2:
        raise ValueError("Enter unique currencies")
    if amount <= 0:
        raise ValueError("Enter amount above 0")

    # Has to convert from curr_1 -> EUR -> curr_2
    result = amount * data["rates"][curr_2] / data["rates"][curr_1]
    print(result)
