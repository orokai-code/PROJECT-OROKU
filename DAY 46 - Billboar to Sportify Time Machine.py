import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

time_machine=input('What year would you like to travel to in YYY-MM-DD format:\n')
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url=f'https://www.billboard.com/charts/hot-100/{time_machine}'

respond=requests.get(url=url,headers=header)
bill_web=respond.text
#print(bill_web)

soup=BeautifulSoup(bill_web,'html.parser')
#print(soup)

title=soup.select(
    'li ul li h3')
#print(title)
bright=[top.getText().strip() for top in title]
#print(bright)

client_id='your client id'
client_secret='your client secret'

sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='Oroku Jesse'
    )
)
user_id = sp.current_user()["id"]
#print(sp.current_user())
#print(user_id)

song_uris = []
year = time_machine.split("-")[0]
for song in bright:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{time_machine} Billboard 100", public=False)
print(playlist)

pant=sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(pant)
