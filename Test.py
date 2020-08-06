import urllib.request
import re

#url = "https://finance.yahoo.com/quote/DIS?p=DIS"
#url = "https://finance.yahoo.com/quote/BAC?p=BAC"
url = "https://finance.yahoo.com/quote/TSLA?p=TSLA"

htmlfile = urllib.request.urlopen(url)
htmlsource = htmlfile.read().decode('utf-8')

regex = '"currentPrice":{"raw":(.+?),'

pattern = re.compile(regex)
price = re.findall(pattern, htmlsource)

#print ("The price of Disney stock is", price)
#print ("The price of BofA stock is", price)
print("The price of Tesla stock is", price)