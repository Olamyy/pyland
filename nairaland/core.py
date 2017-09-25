from __future__ import print_function  # (at top of module)
from nairaland.base import HttpHandler
from bs4 import BeautifulSoup


class Nairaland(HttpHandler):
    def __init__(self, search_result_count=None, default_comment_count=None, show_images=False):
        super(Nairaland, self).__init__()
        self.search_result_count = search_result_count if search_result_count else 10
        self.default_comment_count = default_comment_count if default_comment_count else 10
        self.show_images = show_images if show_images else False
        self.soup = None

    def get_front_page(self, refresh_page=True, count=10):
        soup = self.soup if not refresh_page else self.__initSoup('front_page')
        stories = self.__crawl_front_page(soup, count)
        return stories

    def get_story(self, url=None, story_id=None):
        if story_id:
            self.soup = self.__initSoup('story')
            # title = kwargs.get('title')

        stories = self.__crawl_story(self.soup, url)
        return stories

    def __crawl_story(self, soup, url):
        stories = {}

    def __initSoup(self, initFor):
        url = self._path(initFor)
        result = self._exec_request(url)
        return BeautifulSoup(result, "html.parser")

    def __crawl_front_page(self, soup, count):
        front_page = {}
        front_page_class = soup.find("td", class_='featured w')
        front_page_stories = front_page_class.find_all('a', limit=count)
        for story in front_page_stories:
            front_page['url'] = story.get('href')
            front_page['title'] = story.b.string
        return front_page


nrg = Nairaland()
print(nrg.get_front_page(refresh_page=True))