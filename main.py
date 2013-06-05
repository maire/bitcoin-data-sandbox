from data import bitstamp_public
import time


if __name__ == "__main__":
  bitstamp = bitstamp_public()
  count = 0
  while True:
    bitstamp.refresh()
    count += 1
    weight_asks = 0
    weight_bids = 0
    last = float(bitstamp.ticker['last'])

    for order in bitstamp.orders['asks']:
      bid = float(order[0])
      vol = float(order[1])
      if (bid - last) > 5:
        continue
      elif bid > last:
        tax = (bid - last)
        if (tax < 1):
          tax = 1
      else:
        tax = 1
      weight_asks += (vol / tax)


    for order in bitstamp.orders['bids']:
      bid = float(order[0])
      vol = float(order[1])
      if (last - bid) > 5:
        continue
      if bid < last:
        tax = (last - bid)
        if (tax < 1):
          tax = 1
      else:
        tax = 1
      weight_bids += (vol / tax)

    if (weight_bids > (weight_asks * 8)):
      advise = "BUY"
    elif (weight_asks > (weight_bids * 8)):
      advise = "SELL"
    else:
      advise = "HOLD"

    print "<{0}>".format(advise), "Last", last, "Bid:", weight_bids, "Ask:", weight_asks
    time.sleep(5)