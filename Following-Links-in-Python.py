import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
links = input("Enter URL: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
print("Retrieving:",links)
for x in range(0,count):
  html = urllib.request.urlopen(links).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  links = tags[pos-1].get('href',None)
  print("Retrieving:",links)
  
