import sys
import requests


def main():
    # check for the command line argument provide by the user
    if len(sys.argv) != 2:
        sys.exit("Missing command line argument")

    # Validate the input provide by user is number
    try:
        n_bitconi = float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not number")

    # Fetch the Bitcoin current price in USD

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        current_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Failed to fetch the current price of Bitcoin")

    # Calculate the total cost in USD
    total_cost = n_bitconi * current_price

    # Print the total cost in USD formated to 4 decimal places
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
