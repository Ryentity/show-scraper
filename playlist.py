
class CreateSpotifyPlaylist:

    def __init__(self, playlist_name, auth, username):
        self.playlist_name = playlist_name
        self.auth = auth
        self.username = username

    def generate_playlist_name(self, name):
        """
        Takes initial input show, season, episode, and returns a string name for the
        playlist.
        """
        pass

    def generate_playlist_description(self, name):
        """
        Generate a description explaining the function of the bot and which episode is
        used
        """
        pass

    def get_song_uri(self, song_name):
        """ Query the spotify search api and return the song uri """
        headers = {
                  "Content-Type": "application/json",
                  "Accept": "application/json",
                  "Authorization": self.auth}

        params = {
                 "q": str(song_name),
                 "type": "track",
                 "market": "US"
        }
        response = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
        song_uri = json.loads(response.text)
        return song_uri["tracks"]["items"][0]["uri"]

    def get_song_uris(self, song_name_list):
        """
        Get the song URI for every item on the list. Return a list of song
        URIs.
        """
        self.song_uris = []
        for song_name in song_name_list:
            uri = get_song_uri(song_name)
            self.song_uris.append(uri)

    def create_playlist(self, name, description):
        """
        Create a playlist on spotify with the generated name and
        description
        """
        headers = {
                   "Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": self.auth
        }

        json_data = {
                    "name": name,
                    "description": description,
                    "public": True
        }

        response = requests.post("https://api.spotify.com/v1/users/" + str(self.username) + "/playlists", headers=headers, json=json_data)
        self.playlist_id = json.loads(response.text)
        return self.playlist_id

    def add_playlist_songs(self):
        params = {
                 "uris": ','.join(self.song_uris)
        }

        headers = {
                  "Accept": "application/json",
                  "Content-Type": "application/json",
                  "Authorization": self.auth
        }
        response = requests.post("https://api.spotify.com/v1/playlists/" + self.playlist_id + "/tracks", params=params, headers=headers)
        return response
