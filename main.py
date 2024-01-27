import requests


def get_exchange_rates(target_currency, app_id):
    url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}&symbols={target_currency}"
    response = requests.get(url, params={'app_id': app_id, 'target_currency': target_currency})

    if response.status_code != 200:
        raise Exception(f"Failed API request: {response.status_code}")

    data = response.json()
    rate = data['rates'][target_currency]
    return rate


def convert_currency(amount, target_currency, app_id):
    rate = get_exchange_rates(target_currency, app_id)
    converted_amount = amount * rate
    return round(converted_amount, 2)


def initiate_conversion():
    app_id = '<your_api_key>'
    amount = float(input("Enter the amount you want to exchange: \n"))
    target_currency = input("Enter the target currency: \n").upper()

    try:
        converted_amount = convert_currency(amount, target_currency, app_id)
        print(f"The {amount} in {target_currency} is converted to {converted_amount}")
    except Exception as e:
        print(f"There was an error: {e}")


initiate_conversion()
