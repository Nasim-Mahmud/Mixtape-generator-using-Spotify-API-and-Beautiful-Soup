import os
import pprint
import spotipy
import requests
from datetime import date
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# TODO 1: Retrieving spotify credentials from environment variable
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "https://example.com/"

# TODO 2: Retrieving date from user
year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
day = int(input("Please enter the day: "))

dt = date(year, month, day)  # Use datetime in case of hours, minutes and seconds
print(f"Retrieving data for the date: {dt}, please wait!")

# TODO 3: Scraping data from website
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
# print(musics)

# TODO 4: Creating a list of songs URI and authenticating spotify parameters
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

song_uri = []
pp = pprint.PrettyPrinter(width=41, compact=True)
for music in musics:
    res = sp.search(q=f"track:{music} year:{year}", type="track")
    # pp.pprint(res)
    try:
        uri = res["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
        # pp.pprint(uri)
    except IndexError:
        print(f"Sorry! Can't find the following song: {music}")

# # TODO 5: Creating playlist and adding songs to the playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{dt} Billboard Top 100", public=False)
print(f'Playlist link: {playlist["owner"]["external_urls"]["spotify"]}')
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
print("Success!")
