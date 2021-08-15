from util.validator import validate_url


class UrlObject:
    def __init__(self, url):
        self.url = validate_url(url)