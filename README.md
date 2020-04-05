# Spotipy-gmusicapi-converter
A python script used to import a playlist from Spotify using spotipy and create a Google Play Music playlist using gmusicapi

# Example Usage
```
python3 convert.py
Obtained list of 411 tracks from spotify playlist!
"Sarcastic Sounds - I Don't Sleep" - no result
"Sarcastic Sounds - Make Me Smile" - no result
"Beowülf - Today Is a Gift" - no result
"Beowülf - Please Don't Go" - no result
"Sarcastic Sounds - Suddenly You're in Love" - no result
"Nohidea - falling down (feat. shiloh)" - no result
"Fudasca - I Wrote You a Letter" - no result
...
(Potentially some errors from gmusicapi for songs missing certain info, seems to be a gmusicapi bug - may investigate in the future)
2020-04-05 14:21:15,741 - gmusicapi.Mobileclient1 (shared:279) [ERROR]: the response format for Search was not recognized.
...
"o k h o - Long Espresso" - no result
"Stan Forebee - Perfect Your Own Art" - no result
"Beowülf - Hopeless" - no result
"importmedia - Happy Moments" - no result
"Orca Vibes - Intuition" - no result
"Late June - Running In The Rain" - no result
"Late June - Balcony Pt 2" - no result
Finished searching 411 tracks on Google Play Music
Found: 376, Missing: 35
```

If you've uncommented the last three lines, you should have successfully created a playlist on Google Play Music!
