import os
import spotipy
import requests
from datetime import date
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Retrieving spotify credentials from environment variable
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "https://example.com/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Retrieving date from user
year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
day = int(input("Please enter the day: "))

dt = date(year, month, day)  # Use datetime in case of hours, minutes and seconds
print(dt)

# Scraping data from website
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{dt}")
data = response.text
soup = BeautifulSoup(data, "html.parser")

musics = []
top_music = soup.find_all(name="h3", id="title-of-a-story",
                          class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
for top in top_music:
    top_music = top.get_text().replace("\t", "")
    musics.append(top_music.replace("\n", ""))

music_list = soup.find_all(name="h3", id="title-of-a-story",
                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
for names in music_list:
    music_name = names.get_text().replace("\t", "")
    musics.append(music_name.replace("\n", ""))

print(musics)


