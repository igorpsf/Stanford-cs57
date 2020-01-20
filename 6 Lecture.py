import urllib
import re
import requests
from PIL import Image          # Python Imaging Library
import math
import urllib.request

def areaCircle(radius):
    area = math.pi * radius * radius
    return area

# help() -> modules


img = Image.open('image.jpg')
img = img.rotate(90)
img.save('image90.jpg')

img = Image.new("RGB", (200,100), (200,200,200))
img.save('box.jpg')


url = "https://finance.yahoo.com/quote/DIS?p=DIS"
htmlfile = urllib.request.urlopen(url)
htmlsource = htmlfile.read().decode('utf-8')


regex = '"currentPrice":{"raw":(.+?),'
pattern = re.compile(regex)
price = re.findall(pattern, htmlsource)
print("The price of Disney stock is", price)

response = requests.get("https://www.google.com")
print(response.status_code)

#data = response.json()
#print(response.json())




# #url = "https://finance.yahoo.com/quote/DIS?p=DIS"
# #url = "https://finance.yahoo.com/quote/BAC?p=BAC"
# url = "https://finance.yahoo.com/quote/TSLA?p=TSLA"
#
# htmlfile = urllib.request.urlopen(url)
# htmlsource = htmlfile.read().decode('utf-8')
#
# regex = '"currentPrice":{"raw":(.+?),'
#
# pattern = re.compile(regex)
# price = re.findall(pattern, htmlsource)
#
# #print ("The price of Disney stock is", price)
# #print ("The price of BofA stock is", price)
# print ("The price of Tesla stock is", price)
