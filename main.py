import requests
from bs4 import BeautifulSoup
from datetime import date


# year = int(input("Please enter the year: "))
# month = int(input("Please enter the month: "))
# day = int(input("Please enter the day: "))
#
# dt = date(year, month, day)   # Use datetime in case of hours, minutes and seconds
# print(dt)

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{2021-10-12}")

print(response.text)
