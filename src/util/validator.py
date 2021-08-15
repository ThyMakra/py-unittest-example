import re
from urllib.parse import urlparse


def validate_url(url):
    """
    Validate an HTTP(S) URL

    Helper for use with Colander that validates a URL provided by a user as a
    link for their profile.

    Returns the normalized URL if successfully parsed else raises a ValueError
    """

    parsed_url = urlparse(url)

    if not parsed_url.scheme:
        parsed_url = urlparse('http://{}'.format(url))

    if not re.match('https?', parsed_url.scheme):
        raise ValueError('Invalid URL scheme: {}'.format(parsed_url.scheme))

    if not parsed_url.netloc:
        raise ValueError('Invalid domain name')

    return parsed_url.geturl()
