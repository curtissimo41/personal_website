import requests  # for gathering HTTP info
from bs4 import BeautifulSoup  # for parsing through HTML


class Crypto:
    def __init__(self, name, price, change_24hr, volume):
        self.name = name
        self.price = price
        self.change_24hr = change_24hr
        self.volume = volume
        
    def setprice(self, price):
        self.price = price
        
    def setchange24hr(self, change_24hr):
        self.change_24hr = change_24hr
        
    def setvolume(self, volume):
        self.volume = volume
        
    def setall(self, price, change_24hr, volume):
        self.price = price
        self.change_24hr = change_24hr
        self.volume = volume


def get_crypto_prices():
    """
    Fetches data on crypto prices from coinmarketcap.com & reports the price
    in USD as well as the 24 hour percent change in price.

    TIMING ISSUES WITH THIS FUNCTION:
        -uses triple 'for' loop to gather names of cryptos
        -creates entire list of Crypto objects, then creates a NEW list with
         filtered out Crypto objects (should create filtered list right away)

    :return: Sorted, filtered list of Crypto objects
    """
    reqs = requests.get("https://livemarketcap.com/all")
    soup = BeautifulSoup(reqs.text, 'html.parser')
    soup.prettify()  # Makes HTML code more easily readable

    # List of Cryptos to be included in the filtered list - modify as needed
    checklist = ['adToken', 'Ark', 'Bitcoin', 'Bitcoin Cash', 'Bytecoin',
                 'Cardano', 'Dash', 'Ethereum', 'Ethereum Classic', 'Gas',
                 'Hshare',  'Lisk', 'Litecoin', 'Monero', 'NEM', 'NEO',
                 'OmiseGO', 'Qtum', 'Ripple', 'Siacoin', 'Steem',
                 'Stellar Lumens', 'Stratis', 'TenX', 'Waves', 'Zcash',
                 'ZenCash']

    crypto_list = []  # Initial list of Crypto objects
    sorted_crypto_list = []  # Sorted & filtered list of Crypto objects

    # Loop through items in
    # <div class="columns is-gapless is-mobile coins-table>
    for name in soup.find_all("div",
                              "columns is-gapless is-mobile coins-table"):

        # Check each item in <tbody> of <div class="column is-narrow">
        for bleh in name.find_all("div", "column is-narrow")[0].tbody:

            # Check <span> to find name of crypto
            for meh in bleh.find_all("span"):
                new_curr = Crypto(meh.get_text(), 0, 0, 0)
                crypto_list.append(new_curr)
    """

    # START OF NEW CODE....
    for coin in checklist:
        crypto_list.append(Crypto(coin, 0, 0, 0))
    # END OF NEW CODE
    
    """

    # Loop through <div class="column scrollable"> to get more in-depth info
    for item in soup.find_all("div", "column scrollable"):
        iteration = 0

        # Loop through items under <tbody> tag for price, 24h change, & volume
        for thing in item.tbody:

            price = thing.find_all("td", "has-text-right")[0] \
                         .find_all("span")[0].get_text()
            pct_change = thing.find_all("td", "has-text-right")[1] \
                              .find_all("span")[0].get_text().strip()
            volume = thing.find_all("td", "has-text-right")[2] \
                          .get_text()

            # Assign the price, % change, & volume to current Crypto object
            crypto_list[iteration].setall(price, pct_change, volume)
            iteration += 1

    # sorting, then filtering, the crypto list
    crypto_list.sort(key=lambda x: x.name.upper(), reverse=False)
    for obj in crypto_list:
        if obj.name in checklist:
            sorted_crypto_list.append(obj)
            
    return sorted_crypto_list
