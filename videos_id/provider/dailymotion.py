import re

from videos_id.platform import Platform

class Dailymotion(Platform):
    def __init__(self):
        self.platform = "Dailymotion"

    def check_url(self, url):
        pattern = r'(?:dailymotion\.com(?:\/video|\/hub)|dai\.ly)\/([0-9a-z]+)(?:[\-_0-9a-zA-Z]*)'

        match = re.search(pattern, url, re.IGNORECASE)

        if match:
            return match.group(1)
        else:
            return None
