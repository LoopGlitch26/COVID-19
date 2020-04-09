import requests
from bs4 import BeautifulSoup
print("Welcome to Covid-19 live updates")
website="https://www.worldometers.info/coronavirus/"
a=requests.get(website)
b=BeautifulSoup(a.text, "html.parser")
data_abstract=b.find_all("div", class_="maincounter-number")
print("Total Cases = ", data_abstract[0].text.strip())
print("Total Deaths = ", data_abstract[1].text.strip())
print("Total Recovered = ", data_abstract[2].text.strip())