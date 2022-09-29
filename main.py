import requests
from bs4 import BeautifulSoup
from datetime import date, datetime


year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
day = int(input("Please enter the day: "))

dt = date(year, month, day)
print(dt)
response = requests.get(url="")