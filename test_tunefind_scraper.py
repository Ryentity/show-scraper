import unittest, json
from tunefind import TunefindScraper

class TestTunefindScraper(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.scraper = TunefindScraper('game-of-thrones', True, 3, 1)

    @classmethod
    def takeDown(self):
        pass

    def test_scraper_setup(self):
        self.assertIsInstance(self.scraper.media_name, str)
        self.assertIsInstance(self.scraper.is_show, bool)
        self.assertIsInstance(self.scraper.season, int)
        self.assertIsInstance(self.scraper.episode, int)
        self.assertEqual(self.scraper.media_name, 'game-of-thrones')
        self.assertEqual(self.scraper.is_show, True)
        self.assertEqual(self.scraper.season, 3)
        self.assertEqual(self.scraper.episode, 1)

    def test_get_episode_json_raises_value_error(self):
        self.scraper.media_name = 'game-of-throns'
        with self.assertRaises(ValueError):
            self.scraper.get_episode_json()

    def test_get_episode_json_returns_dict(self):
        self.scraper.get_episode_json()
        self.assertIsInstance(self.scraper.json_data, dict)

    def test_get_episode_ids_creates_episode_list(self):
        with open('tunefind_sample_data.json', 'r') as infile:
            data = json.loads(infile.read())

        self.scraper.json_data = json.loads(data)
        self.scraper.get_episode_ids()
        self.assertIsInstance(self.scraper.episode_ids, list)

    def test_get_song_names_creates_list_of_string_song_names(self):
        with open('tunefind_sample_data.json', 'r') as infile:
            data = json.loads(infile.read())

        self.scraper.json_data = json.loads(data)
        self.scraper.episode_ids = [36336, 36337, 36338, 36339, 36340, 36341, 36342, 36343, 36344, 36345]
        self.scraper.episode_id = 36336

        song_names = self.scraper.get_song_names()
        self.assertIsInstance(self.scraper.song_names, list)
        self.assertEqual(self.scraper.song_names[1], 'White Walkers')

    def test_get_episode_song_names(self):
        self.scraper.get_episode_song_names()
        self.assertIsInstance(self.scraper.episode_songs, list)
        self.assertEqual(self.scraper.episode_songs[0], 'We Are The Watchers On The Wall - From The "Game Of Thrones: Season 2" Soundtrack')
        self.assertEqual(len(self.scraper.episode_songs), 21)


if __name__ == '__main__':
    unittest.main()
