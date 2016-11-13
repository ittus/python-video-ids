from abc import ABCMeta, abstractclassmethod

class Platform:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.platform = None

    @abstractclassmethod
    def check_url(self, url):
        pass