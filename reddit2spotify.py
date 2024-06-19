import os
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging
import time

logging.basicConfig(level=logging.INFO)

# set your environment variables to each of these
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
SCOPE = 'playlist-modify-public'

# this is a file that will contain a list of songs (Title - Artist)
SONGS_FILE = 'songs.txt'

# this file is a counter to help with naming playlists
COUNTER_FILE = 'playlist_counter.txt'

def read_counter():
    try:
        with open(COUNTER_FILE, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0

def write_counter(counter):
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))

def create_spotify_playlist(songs):
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri=REDIRECT_URI,
                                                       scope=SCOPE))

        # get login info
        user = sp.current_user()
        username = user['id']

        # read counter.txt and increment
        counter = read_counter()
        counter += 1
        write_counter(counter)

        # Create a new playlist with a unique number
        playlist_name = f'My Automated Playlist {counter}'
        playlist_description = 'Created by a script!'
        playlist = sp.user_playlist_create(username, playlist_name, public=True, description=playlist_description)

        for song in songs:
            song = song.strip()
            if not song:
                continue
            
            if ' - ' in song:
                parts = song.split(' - ')
            elif ' by ' in song:
                parts = song.split(' by ')
            else:
                logging.warning(f"Invalid format: '{song}'. Skipping...")
                continue  # Skip lines that don't match expected format
            
            if len(parts) != 2:
                logging.warning(f"Invalid format: '{song}'. Skipping...")
                continue
            
            title, artist = parts
            # remove comments or extra text within parentheses
            title = re.sub(r"\(.*?\)", "", title).strip()
            artist = re.sub(r"\(.*?\)", "", artist).strip()

            # check spotify
            try:
                results = sp.search(q=f"track:{title} artist:{artist}", type='track')
                items = results['tracks']['items']
                if items:
                    track_uri = items[0]['uri']
                    sp.playlist_add_items(playlist['id'], [track_uri])
                    logging.info(f"Added {title} by {artist} to the playlist.")
                else:
                    logging.info(f"Couldn't find {title} by {artist} on Spotify.")
            except spotipy.exceptions.SpotifyException as e:
                if e.http_status == 429:  # i'm not trying to lose my money in api requests
                    retry_after = int(e.headers.get('Retry-After', 1))
                    logging.warning(f"Rate limit exceeded. Retrying after {retry_after} seconds.")
                    time.sleep(retry_after)
                    continue  # try again
                else:
                    logging.error(f"Spotify API error: {e}")
                    break  
                
        logging.info(f"Playlist '{playlist_name}' has been created and populated with songs.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    try:
        with open(SONGS_FILE, 'r') as f:
            songs = f.readlines()

        create_spotify_playlist(songs)
        
    except FileNotFoundError:
        logging.error(f"The file {SONGS_FILE} was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
