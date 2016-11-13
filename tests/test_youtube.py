import unittest

from videos_id.video_info import VideoInfo

class YoutubeTest(unittest.TestCase):
    def setUp(self):
        self.video_info = VideoInfo()

    def tearDown(self):
        self.video_info = None

    def test_normal_url_correct(self):
        url = 'https://www.youtube.com/watch?v=gb5HmcdIHb8'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "gb5HmcdIHb8")
        self.assertEqual(self.video_info.platform, "Youtube")

    def test_embed_url_correct(self):
        url = 'http://www.youtube.com/embed/gb5HmcdIHb8?rel=0'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "gb5HmcdIHb8")
        self.assertEqual(self.video_info.platform, "Youtube")

    def test_shorten_url_correct(self):
        url = 'http://youtu.be/gb5HmcdIHb8'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "gb5HmcdIHb8")
        self.assertEqual(self.video_info.platform, "Youtube")


if __name__ == '__main__':
    unittest.main()