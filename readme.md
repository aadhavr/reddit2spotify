# Text to Spotify Playlist Convertor

I like to get my music recommendations from the internet. But, Spotify is very laggy and searching everything up and adding them to a playlist can take hours for long lists. This script that creates a Spotify playlist from a list of songs provided in a `songs.txt` file. The script uses the Spotify Web API to search for the songs and add them to a new playlist.

## Prerequisites

- Python 3.x
- A Spotify account
- Spotify API credentials (Client ID, Client Secret, and Redirect URI)

## Setup

### Step 1: Clone the Repository

```sh
git clone https://github.com/yourusername/reddit2spotify.git
cd reddit2spotify
```

### Step 2: Install Required Python Packages

```sh
pip install spotipy
```

### Step 3: Set Up Spotify API Credentials

You need to create a Spotify developer application to get your Client ID, Client Secret, and Redirect URI.

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and log in.
2. Click on "Create an App".
3. Fill in the required details and click "Create".
4. Once your app is created, you will see your Client ID and Client Secret.
5. Set your Redirect URI to `http://localhost:8888/callback`.

### Step 4: Export Your Spotify API Credentials

Export your Spotify API credentials as environment variables. You can add the following lines to your shell configuration file (`.zshrc`, `.bashrc`, etc.):

```sh
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
```

Then, source your shell configuration file to apply the changes:

```sh
source ~/.zshrc  # or ~/.bashrc
```

### Step 5: Prepare Your Songs List

Create a `songs.txt` file in the root directory of the repository. Each line in the file should contain a song in the format `Title - Artist` or `Title by Artist`. Here is an example:

```txt
Your Arms Around Me - Jens Lekman
Feel You - Julia Holter
Movies - Weyes Blood
Take Your Carriage Clock and Shove It - Belle and Sebastian
Consequence - The Notwist
Boys of Melody - The Hidden Cameras
Hilli (At the Top of the World) featuring Lee Hazlewood - amiina
Nearly Midnight, Honolulu - Neko Case
Starálfur - Sigur Rós
All the Colors of the Dark - Marissa Nadler
Green Grass Of Tunnel - Múm
Both Sides Now - Judy Collins
God Knows (You Gotta Give To Get) - El Perro Del Mar
Spinning Away - Brian Eno
Light Years - The National
Wait - M83
The Voyager - Jenny Lewis
Stargazer - The Zephyrs
Blue Moon - Big Star
Now That I'm Older - Sufjan Stevens
Stardust - Nat King Cole
```

## Running the Script

### Method 1: Directly from Terminal

```sh
python3 reddit2spotify.py
```

### Method 2: Using a Shell Script

Create a shell script named `run_spotify.sh` to simplify running the Python script:

```sh
#!/bin/bash

# Navigate to the directory containing the Python script and songs.txt
cd /path/to/your/directory

# Run the Python script
python3 reddit2spotify.py
```

Make the shell script executable:

```sh
chmod +x /replace/with/actual/path/run_spotify.sh
```

Then, you can run the script with:

```sh
./run_spotify.sh
```

### Method 3: Using Aliases

Add the following aliases to your shell configuration file (`.bashrc`, `.zshrc`, etc.):

```sh
# Alias to open the songs.txt file with your preferred text editor
alias editsongs='code /path/to/your/directory/songs.txt'  # Replace 'code' with your preferred text editor. 

# Alias to run the shell script
alias runspotify='/path/to/your/directory/run_spotify.sh'
```

Source your shell configuration file:

```sh
source ~/.zshrc  # or ~/.zshrc
```

Now you can use the following commands:

- To open the `songs.txt` file:

  ```sh
  editsongs
  ```

- To run the script:

  ```sh
  runspotify
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
