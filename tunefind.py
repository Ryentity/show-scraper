import requests, json

artists = {'artists': ['ariana grande', 'blackpink', '21 savage & metro boomin', 'juice wrld', 'eminem', 'kanye west', 'drake', 'travis scott', 'bts', 'joji', 'taylor swift', 'pop smoke', 'kendrick lamar', 'machine gun kelly', 'the weeknd', 'bryson tiller', 'lil peep', 'cardi b', 'xxxtentacion', 'frank ocean', 'lana del rey', 'shawn mendes', 'internet money', 'j. cole', 'freeze corleone', 'trippie redd', 'damso', 'justin bieber & benny blanco', 'the beatles', 'melanie martinez', 'justin bieber', 'gorillaz', 'harry styles', 'slava marlow', 'lil uzi vert', 'mac miller', 'little mix', 'billie eilish', '2pac', 'lil wayne', '$suicideboy$', 'nf', 'polo g', 'corpse', 'jay-z', 'scriptonite', 'bruce springsteen', 'tyler, the creator', 'larray', 'bring me the horizon', 'tory lanez', 'husky', '13 organise', 'nicki minaj', 'megan thee stallion', 'beyonce', 'arctic monkeys', 'lany', 'slait, tha supreme & young miles', 'one direction', 'logic', 'jack harlow', 'sam smith', 'slait & young miles', 'future', 'radiohead', 'queen', 'fleetwood mac', 'joyner lucas', 'pink floyd', 'mecna', 'salem ilese', 'ghostmane', 'giveon', 'sza', 'michael jackson', 'ty dolla $ign', 'post malone', 'nirvana', 'lil baby', 'kizaru', 'playboi carti', 'lady gaga', 'young thug', 'julie and the phantoms cast', 'big sean', 'morgenshtern & timati', 'luke combs']}

class TunefindScraper:

    def __init__(self, media_name, is_show, season, episode):
        """
        Initiates scraper object with show/movie name, is_show boolean, season and episode
        """
        self.media_name = media_name
        self.is_show = is_show
        self.season = season
        self.episode = episode

    def get_episode_json(self):
        """
        Sends a request to the tunefind API to get JSON data that contains episode ids
        get_episode_ids should be called on the data and the result should be passed
        to the get_song_names function
        """

        params = {
                 "fields": "theme-song,episodes,song-events",
                 "metatags": 1
        }


        data = requests.get('https://www.tunefind.com/api/frontend/show/' + self.media_name + \
        '/season/' + str(self.season), params=params)

        data_dict = json.loads(data.text)

        # Returns ValueError if api throws a bad response
        if type(data_dict) == list:
            raise ValueError('Show and episode not found')

        self.json_data = data_dict

    def get_episode_ids(self):
        """
        Finds episode ids from tunefind json data
        """
        self.episode_ids = []

        for item in self.json_data['episodes']:
            self.episode_ids.append(item['id'])

        self.episode_id = self.episode_ids[self.episode - 1]

    def get_song_names(self):
        data = requests.get('https://www.tunefind.com/api/frontend/episode/' + str(self.episode_id) +'?fields=song-events')
        data_dict = json.loads(data.text)

        self.song_names = []

        for song in data_dict['episode']['song_events']:
            self.song_names.append(song['song']['name'])


    def get_episode_song_names(self):
        """
        Return a list of song names from a specific episode

        this method is the guide to testing get_song_names
        """
        self.get_episode_json()
        self.get_episode_ids()
        self.get_song_names()

        self.episode_songs = []
        theme_song = self.json_data["theme_song"]["name"]

        for song in self.song_names:
            self.episode_songs.append(song)
        self.episode_songs.append(theme_song)

        for song in self.song_names:
            self.episode_songs.append(song)
