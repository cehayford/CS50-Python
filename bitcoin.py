import sys
import requests

if len(sys.argv) == 2:
    try:
        number_of_bitcoins = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)
try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    data = response.json()["bpi"]["USD"]
    current_price = data["rate_float"]

    total_amount = number_of_bitcoins * current_price

    formatted_cost = f"${total_amount:,.4f}"

    print(formatted_cost)
except requests.RequestException:
    print('RequestException')
    sys.exit(1)