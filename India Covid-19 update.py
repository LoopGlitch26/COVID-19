import requests
from bs4 import BeautifulSoup
print("Welcome to Covid-19 live updates in India")
website="https://www.worldometers.info/coronavirus/country/india/"
a=requests.get(website)
b=BeautifulSoup(a.text, "html.parser")
data_abs=b.find_all("div", class_="maincounter-number")
print("Total Cases = ", data_abs[0].text.strip())
print("Total Deaths = ", data_abs[1].text.strip())
print("Total Recovered = ", data_abs[2].text.strip())
