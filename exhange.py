import requests
DEFAULT_KEY = 'fca_live_gcb0HOci2hThCuxjmjlqtwO4jyc6wIeYKzyE5XAh'
def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey={DEFAULT_KEY}&base_currency={base_currency}&currencies={target_currency}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    rate = data['data'][target_currency]
    return rate

def convert_currency(amount, rate):
    return amount * rate

def main():
    api_key = DEFAULT_KEY
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    amount = float(input(f"Enter amount in {base_currency}: "))

    try:
        rate = get_exchange_rate(api_key, base_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except KeyError:
        print("Error: Invalid currency code or API response")
    except Exception as err:
        print(f"Error occurred: {err}")

if __name__ == '__main__':
    main()
