from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
import os

Year = input("Enter the Year you want to travel to...(YYYY-MM-DD) \n")
Markup_response=requests.get(url=f"https://www.billboard.com/charts/hot-100/{Year}/#")
soup=BeautifulSoup(Markup_response.text,"html.parser")

song_dict={tag.text.strip():tag.find_next_sibling().text.strip() for tag in soup.select(selector="li .c-title")}

# print(song_dict)

client_secret=os.environ["CLIENT_SECRET"]
client_id=os.environ["CLIENT_ID"]
redirect_url=os.environ["REDIRECT_URL"]

token=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_url)
token=token.get_cached_token()["access_token"]

# print(token)


header1={
    "Content-Type": "application/x-www-form-urlencoded"
}

spotify_endpoint_user="https://api.spotify.com/v1/users"
spotify_user_id=os.environ['USER_ID']

header={
    "Authorization": f"Bearer {token}",
}

parameters={
    "name":f"Nostalgia Playlist {Year} ",
    "description":"A playlist created using Web scraping and the spotify API"
}

response=requests.post(f"{spotify_endpoint_user}/{spotify_user_id}/playlists",headers=header,json=parameters)
response.raise_for_status()
# print(response)
playlist_id=response.json()["id"]

search_endpoint="https://api.spotify.com/v1/search"

for song in song_dict:

    body={
        "q":f"track:{song} artist:{song_dict[song]} year:{Year.split('-')[0]}",
        "type":"track",
        "market":"IN",

    }

    response=requests.get(url=search_endpoint,params=body,headers=header)
    data=response.json()
    response.raise_for_status()
    # print(data['tracks'])
    try:
        song_uri=data['tracks']["items"][0]['uri']
    except IndexError:
        continue
    except KeyError:
        continue

    add_item_playlist=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    body={
        "uris":song_uri
    }

    response=requests.post(url=add_item_playlist,params=body,headers=header)
    # print(response.text)