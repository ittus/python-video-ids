from videos_id.provider.dailymotion import Dailymotion
from videos_id.provider.vimeo import Vimeo
from videos_id.provider.youtube import Youtube

class VideoInfo(object):
    def __init__(self):
        dailymotion = Dailymotion()
        youtube = Youtube()
        vimeo = Vimeo()
        self.platform_list = [dailymotion, youtube, vimeo]
        self.platform = None
        self.video_id = None

    def check_video_id(self, url):
        for platform in self.platform_list:
            video_id = platform.check_url(url)
            if video_id:
                self.video_id = video_id
                self.platform = platform.platform
                return video_id

        self.video_id = None
        self.platform = None
        return self.video_id