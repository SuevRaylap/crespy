from crespy import get_crest_root

root = get_crest_root('crespy-sample')

print(root)

specs = root.industry.specialities.href
specs.load()

print(specs)

regions = root.regions.href
regions.load()

print(regions)

for items in regions['items']:
#  #print items.name
  if items.name == 'B-R00004':
    print("it worked")
    print(items.name)

prices = root.marketPrices.href
prices.load()

print(prices)

# you need to do it this way because items is a method on the collection class
for item in prices['items']:
  if item.type.id == 29668:
    print("The price of PLEX is too damn high: {:,} ISK".format(item.averagePrice))
