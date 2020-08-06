import urllib
#import urllib.request
#import urllib.urlopen
import re

url = "https://finance.yahoo.com/quote/DIS?p=DIS"

htmlfile = urllib.urlopen(url)
htmlsource = htmlfile.read()

regex = '"currentPrice":{"raw":(.+?),'

pattern = re.compile(regex)
price = re.findall(pattern, htmlsource)
print ("The price of Disney stock is", price)

# import urllib
# import re
#
# url = "https://finance.yahoo.com/quote/DIS?p=DIS"
# htmlfile = urllib.urlopen(url)
# htmlsource = htmlfile.read()
#
# regex = '"currentPrice":{"raw":(.+?),'
# pattern = re.compile(regex)
# price = re.findall(pattern, htmlsource)
# print ("The price of Disney stock is", price)