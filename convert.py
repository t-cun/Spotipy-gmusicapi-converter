# Make sure these exist in your environment for spotipy!
# export SPOTIPY_CLIENT_ID="YOUR_SPOTIFY_CIENT_ID"
# export SPOTIPY_CLIENT_SECRET="YOUR_SPOTIFY_CLIENT_SECRET"

from gmusicapi import Mobileclient
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_tracks = []

# Spotify playlist ID that you would like to convert
# Currently, this playlist must be public.
# I've obtained this via URL from browser web-app
# (i.e. https://open.spotify.com/playlist/7jNaXgyXgipE4RNcNCBYmW)
spotify_playlist_id = '7jNaXgyXgipE4RNcNCBYmW'

# Print
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        # print(f" {i} {track['artists'][0]['name']} {track['name']}")
        track_info = f"{track['artists'][0]['name']} - {track['name']}"
        spotify_tracks.append(track_info)
    return len(tracks['items'])

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.playlist(spotify_playlist_id,  fields="tracks,next")
tracks = results['tracks']
show_tracks(tracks)

num_tracks = len(tracks['items'])
while tracks['next']:
    tracks = sp.next(tracks)
    # spotify_tracks.append(tracks)
    num_tracks += show_tracks(tracks)

print(f"Obtained list of {len(spotify_tracks)} tracks from spotify playlist!")

api = Mobileclient()

# Run perform_oath() the first time!
# api.perform_oauth()

api.oauth_login('YOUR_GOOGLE_PLAY_AUTH_TOKEN')

missing_data = 0
google_play_ids = []

for track in spotify_tracks:
    result = {}
    try:
        result = api.search(track, max_results=1)
    except:
        # Currently there are some gmusicapi exceptions here that show up on stdout
        # but the app will continue searching each track and eventually complete
        print(f'Error searching "{track}"')

    if(not result['song_hits'] or not len(result['song_hits'])):
        missing_data += 1
        print(f'"{track}" - no result')
    else:
        google_play_ids.append(result['song_hits'][0]['track']['storeId'])

# Print info about how many of the songs were successfully found on google play
print(f"Finished searching {len(google_play_ids) + missing_data} tracks on Google Play Music")
print(f"Found: {len(google_play_ids)}, Missing: {missing_data}")

## Uncomment these if you want to create a playlist on Google Play Music!
# playlist_name = 'Lo-Fi Dialogue'
# playlist_id = api.create_playlist(playlist_name)
# api.add_songs_to_playlist(playlist_id, google_play_ids)
