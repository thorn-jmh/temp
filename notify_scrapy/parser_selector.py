import re
from urllib.parse import splittype, splithost


class Page:
    def __init__(self, parser, regex=None):
        self.parser = parser
        if regex:
            self.regex = re.compile(regex)
        else:
            self.regex = None

    def validate(self, path):
        if self.regex:
            return self.regex.match(path)
        return True


hosts = {}


def page(host: str, path_regex: str = None):
    def decorator(func):
        if hosts.get(host) is None:
            hosts[host] = []
        hosts[host].append(Page(func, path_regex))
        return func

    return decorator


def select_parser(url):
    type, rest = splittype(url)
    host, path = splithost(rest)
    pages = hosts.get(host)
    if not pages:
        return None

    for page in pages:
        if page.validate(path):
            return page.parser
    return None
