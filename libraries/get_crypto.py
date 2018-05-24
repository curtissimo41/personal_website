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


def get_crypto_prices():
	"""
    Fetches data on crypto prices from livemarketcap.com & reports the price
    in USD as well as the 24 hour percent change in price.

    TIMING ISSUES WITH THIS FUNCTION:
        -uses double 'for' loop to gather names of cryptos
        -creates entire list of Crypto objects, then creates a NEW list with
         filtered out Crypto objects (should create filtered list right away)

    :return: Sorted, filtered list of Crypto objects
    """
	url = "https://coinmarketcap.com/all/views/all"
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
		              '(KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
	reqs = requests.get(url, headers=headers)
	soup = BeautifulSoup(reqs.text, 'html.parser')
	soup.prettify()  # Makes HTML code more easily readable

	# List of Cryptos to be included in the filtered list - modify as needed
	checklist = ['ADA', 'ADT', 'ARK', 'BTC', 'BCH', 'BCN', 'DASH', 'ETH', 'ETC',
	             'GAS', 'HSR', 'LSK', 'LTC', 'NEO', 'OMG', 'PAY', 'QTUM', 'SC',
	             'STEEM', 'STRAT', 'WAVES', 'XEM', 'XLM', 'XMR', 'XRP', 'ZEC',
	             'ZEN']

	crypto_list = []  # Initial list of Crypto objects

	"""
	# Loop through <div class="column scrollable"> to get more in-depth info
	for item in soup.find_all("div", "column scrollable"):
		# Loop through items under <tbody> tag for price, 24h change, & volume
		for crypto in item.tbody:
			symbol = crypto.find_all("td", "has-text-right")[3] \
				.get_text().split()[1]
			if symbol in checklist:
				price = crypto.find_all("td", "has-text-right")[0] \
					.find_all("span")[0].get_text()
				pct_change = crypto.find_all("td", "has-text-right")[1] \
					.find_all("span")[0].get_text().strip()
				volume = crypto.find_all("td", "has-text-right")[2] \
					.get_text()

				# Assign the symbol, price, % change, & volume to current
				# Crypto object
				new_curr = Crypto(symbol, price, pct_change, volume)
				crypto_list.append(new_curr)

		break
	"""

	# Loop through <div class="table-responsive compact-name-column"> to get
	# more in-depth info
	for item in soup.find_all("div", "table-responsive compact-name-column"):
		# Loop through each row in the table containing crypto information
		for item2 in item.find_all(id="currencies-all"):
			# Loop through each piece of info provided for each crypto
			for item3 in item2.tbody.find_all("tr"):
				symbol = item3.find("span").get_text()
				if symbol in checklist:
					price = item3.find_all("td", "no-wrap text-right")[0] \
						.find("a").get_text()
					pct_change = item3.find_all("td")[8].get_text()
					volume = item3.find_all("td")[6].get_text().strip()
					# Assign the symbol, price, 24h % change, & volume to
					# current Crypto object
					new_curr = Crypto(symbol, price, pct_change, volume)
					crypto_list.append(new_curr)
			break
		break

	# sorting, then filtering, the crypto list
	crypto_list.sort(key=lambda x: x.name.upper(), reverse=False)

	return crypto_list
