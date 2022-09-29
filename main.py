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

top_music = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
for top in top_music:
    top_music = top.get_text().replace("\n", "")
    print(top_music)
music_list = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

for names in music_list:
    music_name = names.get_text().replace("\n", "")
    print(music_name.replace("    ", ""))
