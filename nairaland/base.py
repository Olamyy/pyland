import requests


class HttpHandler(object):
    def __init__(self):
        self._content_type = "application/json"
        self._base_url_map = {
            "front_page": "http://www.nairaland.com/",
            "search": "http://www.nairaland.com/search?q=<query>&search=Search",
            "category": "http://www.nairaland.com/<category>",
            "story": "http://www.nairaland.com/<id>",
            "story_url": "http://www.nairaland.com/<url>",
            "comment": "http://www.nairaland.com/<id><title>#<comment_id>",
        }

    def _path(self, path):
        url_path = self._base_url_map.get(path)
        return url_path

    def _exec_request(self, url):
        response = requests.get(url,verify=True)
        if response.status_code in [200, 201]:
            content = response.content
            return content
