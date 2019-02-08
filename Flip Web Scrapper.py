import requests
import json
from bs4 import BeautifulSoup

def flipkart(s):

    for i in range(1,11):
        url='https://www.flipkart.com/search?q='+str(s)+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
        data=requests.get(url)
        plain_text=data.text
        soup=BeautifulSoup(plain_text,"html.parser")
        j=1
        for digits in soup.find_all('a',{'class':'_2cLu-l'}):
            print(j,digits.get('title'))
            j+=1
flipkart(input("Enter product name: "))

for link in soup.findAll('a',{'class':'_2cLu-l'}):
            print(link.get('title'))
            i = i + 1