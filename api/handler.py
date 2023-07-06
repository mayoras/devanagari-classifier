from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl
from os import path


"""
Simple HTTP Web Handler as the Gateway to the module
"""


class WebRequestHandler(BaseHTTPRequestHandler):
    @cached_property
    def url(self):
        # Parse the url
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        # Parse the query data
        return dict(parse_qsl(self.url.path))

    @cached_property
    def form_data(self):
        # parse the POST form data
        return dict(parse_qsl(self.post_data.decode("utf-8")))

    @cached_property
    def post_data(self):
        # Read the post data from buffer
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    @cached_property
    def cookies(self):
        # read the request cookie
        return SimpleCookie(self.headers.get("Cookie"))

    def do_GET(self):
        print(self.url.path.split(sep="/")[1:])
