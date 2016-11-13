import re

from videos_id.platform import Platform

class Youtube(Platform):
    def __init__(self):
        self.platform = "Youtube"

    def check_url(self, url):
        pattern = r'((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)'

        match = re.search(pattern, url, re.IGNORECASE)

        if match:
            return match.group()
        else:
            return None
