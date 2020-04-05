from gmusicapi import Mobileclient
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_tracks = []

# Print
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        # print(f" {i} {track['artists'][0]['name']} {track['name']}")
        track_info = f" {track['artists'][0]['name']} {track['name']}"
        spotify_tracks.append(track_info)
    return len(tracks['items'])


sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.playlist('7jNaXgyXgipE4RNcNCBYmW',  fields="tracks,next")
tracks = results['tracks']
show_tracks(tracks)

num_tracks = len(tracks['items'])
while tracks['next']:
    tracks = sp.next(tracks)
    # spotify_tracks.append(tracks)
    num_tracks += show_tracks(tracks)

print(f"Total tracks: {num_tracks}")
print(f'Count: {len(spotify_tracks)}')
