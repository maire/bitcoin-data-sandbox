import grequests

public_urls = [
  'https://www.bitstamp.net/api/ticker/',
  'https://www.bitstamp.net/api/order_book/',
  'https://www.bitstamp.net/api/transactions/'
]

class bitstamp_public:
  ticker = {}
  orders = {}
  trans = {}
  def refresh(self):
    results = grequests.map(grequests.get(u) for u in public_urls)
    for result in results:
      if result.url == "https://www.bitstamp.net/api/ticker/":
        self.ticker = result.json()
      elif result.url == "https://www.bitstamp.net/api/order_book/":
        self.orders = result.json()
      elif result.url == "https://www.bitstamp.net/api/transactions/":
        self.trans = result.json()
