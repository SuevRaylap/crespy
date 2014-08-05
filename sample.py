from crespy import get_crest_root

root = get_crest_root()

print root

specs = root.industry.specialities.href
specs.load()
#print specs

prices = root.marketPrices.href
prices.load()

# you need to do it this way because items is a method on the collection class
for item in prices['items']:
  if item.type.id == 29668:
    print "The price of PLEX is too damn high: {:,} ISK".format(item.averagePrice)

