import requests
import csv 
import datetime

assert __name__ != "__main__", "cannot be accessed directly"

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

    # Make the request
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()  # Raise HTTPError for bad responses
    info = response.json()  # Parse JSON response
    data = info["data"]

    list_2D = [["Name", "Symbol", "Price", "Price Change (24 hr)", "Volume (24 hr)", "Market Cap"]]
    prices = []
    pc_24 = []
    for coin in data:
        entry = [coin['name'],coin['symbol'],coin['quote']['USD']['price'],coin['quote']['USD']['percent_change_24h'],coin['quote']['USD']['volume_24h'],coin['quote']['USD']['market_cap']]
        list_2D.append(entry)
        prices.append(coin['quote']['USD']['price'])
        pc_24.append(coin['quote']['USD']['percent_change_24h'])
    
    top_five_by_MC = [["Rank","Name", "Symbol", "Price", "Price Change (24 hr)", "Volume (24 hr)", "Market Cap"]]
    for i in range(1,6):
        top_five_by_MC.append([i]+list_2D[i])
    
    min = max = 0
    for val in range(len(pc_24)):
        if abs(pc_24[i]) < abs(pc_24[min]):
            min = i
        if abs(pc_24[i]) > abs(pc_24[max]):
            max = i

    with open("coin_data.csv", "w", newline="") as file:

        writer = csv.writer(file)
        
        writer.writerow([f"most recent timestamp: {datetime.datetime.now()}"])
        writer.writerow([])

        writer.writerows(list_2D) 

        writer.writerow([])
        writer.writerow(["Top five by market capitalization:"])
        writer.writerows(top_five_by_MC)

        writer.writerow([])
        writer.writerow([f"Current average price (USD) of top 50 cryptocurrencies: {sum(prices)/50}"])

        writer.writerow([])
        writer.writerow([f"Cryptocurrency with highest price change: {list_2D[max+1][0]}, {list_2D[min+1][1]}, {list_2D[min+1][3]}"])
        writer.writerow([f"Cryptocurrency with lowest price change: {list_2D[min+1][0]}, {list_2D[min+1][1]}, {list_2D[min+1][3]}"]) 