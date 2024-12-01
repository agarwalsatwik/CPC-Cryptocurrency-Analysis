import requests
import csv  

# Replace with your actual API key
api_key = "96c9a13f-f3bd-43eb-80b1-00649a66c046"
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Headers for the API call
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": api_key,
}

# Query parameters (optional)
parameters = {
    "start": "1",  # Starting rank (1 = top-ranked cryptocurrency)
    "limit": "50",  # Number of cryptocurrencies to fetch
    "convert": "USD",  # Currency for conversion
}

def cpc_main():

    assert __name__ != "__main__"
    # Make the request
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()  # Raise HTTPError for bad responses
    data = response.json()  # Parse JSON response
    # for coin in data["data"]:
    #     print(f"Name: {coin['name']}, Symbol: {coin['symbol']}, Price: ${coin['quote']['USD']['price']}, Price Change (24 hr): {coin['quote']['USD']['percent_change_24h']}, Volume (24 hr): {coin['quote']['USD']['volume_24h']}, Market Cap: {coin['quote']['USD']['market_cap']}")
    #     print(f"Name: {coin['name']}, Market Cap: {coin['quote']['USD']['market_cap']}")

    list_2D = [["Name", "Symbol", "Price", "Price Change (24 hr)", "Volume (24 hr)", "Market Cap"]]

    for coin in data["data"]:
        entry = [coin['name'],coin['symbol'],coin['quote']['USD']['price'],coin['quote']['USD']['percent_change_24h'],coin['quote']['USD']['volume_24h'],coin['quote']['USD']['market_cap']]
        list_2D.append(entry)

    # Writing each inner list as a row in the CSV file
    with open("coin_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list_2D)  # Write all rows from the 2D list
