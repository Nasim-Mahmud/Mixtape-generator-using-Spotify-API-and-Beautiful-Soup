import requests
from bs4 import BeautifulSoup
from datetime import date


# year = int(input("Please enter the year: "))
# month = int(input("Please enter the month: "))
# day = int(input("Please enter the day: "))
#
# dt = date(year, month, day)   # Use datetime in case of hours, minutes and seconds
# print(dt)

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{2022-10-1}")

data = response.text
soup = BeautifulSoup(data, "html.parser")

music = soup.find_all(name="h3", class_="c-title a-no-trucate")
print(music)
