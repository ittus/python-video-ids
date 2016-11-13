import unittest

from videos_id.video_info import VideoInfo

class DailymotionTest(unittest.TestCase):
    def setUp(self):
        self.video_info = VideoInfo()

    def tearDown(self):
        self.video_info = None

    def test_normal_url_correct(self):
        url = 'http://www.dailymotion.com/video/x51lfw0'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "x51lfw0")
        self.assertEqual(self.video_info.platform, "Dailymotion")

    def test_full_url_correct(self):
        url = 'http://www.dailymotion.com/video/x51lfw0_harvey-sutherland-bermuda-live-at-dimensions-2016_music'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "x51lfw0")
        self.assertEqual(self.video_info.platform, "Dailymotion")

    # def test_embed_url_correct(self):
    #     url = 'http://www.dailymotion.com/embed/video/x51lfw0'
    #     video_id = self.video_info.check_video_id(url)
    #     self.assertEqual(video_id, "x51lfw0")
    #     self.assertEqual(self.video_info.platform, "Dailymotion")

    def test_shorten_url_correct(self):
        url = 'http://dai.ly/x51lfw0'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "x51lfw0")
        self.assertEqual(self.video_info.platform, "Dailymotion")


if __name__ == '__main__':
    unittest.main()