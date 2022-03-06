from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
user_request = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{user_request}/"

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

response = requests.get(url=URL)
raw_data = response.text

soup = BeautifulSoup(raw_data, "html.parser")

top_songs = soup.find_all(
    name="div", class_="o-chart-results-list-row-container")

songs = [song.find(name="h3", id="title-of-a-story").getText().strip()
         for song in top_songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:5500/",
        show_dialog=True,
        cache_path="token.txt",
        scope="playlist-modify-private"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = user_request.split("-")[0]
song = songs[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{user_request} Billboard Top 100", public=False)

sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist["id"], tracks=song_uris)
