import unittest

from videos_id.video_info import VideoInfo

class VimeoTest(unittest.TestCase):
    def setUp(self):
        self.video_info = VideoInfo()

    def tearDown(self):
        self.video_info = None

    def test_normal_url_correct(self):
        url = 'http://vimeo.com/88888888'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "88888888")
        self.assertEqual(self.video_info.platform, "Vimeo")

    def test_embed_url_correct(self):
        url = 'http://player.vimeo.com/video/88888888'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "88888888")
        self.assertEqual(self.video_info.platform, "Vimeo")

    def test_channel_url_correct(self):
        url = 'http://vimeo.com/channels/staffpicks/88888888'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "88888888")
        self.assertEqual(self.video_info.platform, "Vimeo")

    def test_group_url_correct(self):
        url = 'https://vimeo.com/groups/name/videos/11111111'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "11111111")
        self.assertEqual(self.video_info.platform, "Vimeo")

    def test_album_url_correct(self):
        url = 'https://vimeo.com/album/2222222/video/11111111'
        video_id = self.video_info.check_video_id(url)
        self.assertEqual(video_id, "11111111")
        self.assertEqual(self.video_info.platform, "Vimeo")

if __name__ == '__main__':
    unittest.main()