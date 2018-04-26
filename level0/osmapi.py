import requests
import time
import os

LEVEL0_API = 'http://level0.osmz.ru/console_auth.php'


class OsmApi(object):
    def __init__(self, path):
        if not os.path.isdir(path):
            os.makedirs(path)
        self.filename = os.path.join(path, 'tokens')
        self.read_tokens()

    def read_tokens(self):
        self.token = None
        self.secret = None
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.token = f.readline()
                    self.secret = f.readline()
            except IOError:
                self.token = None
                self.secret = None

    def write_tokens(self):
        if not self.token or not self.secret:
            return
        with open(self.filename, 'w') as f:
            f.write(self.token + '\n')
            f.write(self.secret + '\n')

    def authorize(self):
        """Sends a call to web level0 and waits for a response."""
        if self.authorized(True):
            return True
        rid = 'askdfjhsaklfhjalsfjhdas'  # TODO: make a good one
        resp = requests.get(LEVEL0_API, {'action': 'login', 'rid': rid})
        time.sleep(10)
        attempts = 0
        while True:
            attempts += 1
            resp = requests.get(LEVEL0_API, {'action': 'check', 'rid': rid})
            if resp:
                break
            if attempts == 10:
                break
            time.sleep(1)
        return False

    def authorized(self, test=False):
        if not self.token or not self.secret:
            return False
        if not test:
            return True
        # TODO: call /user/details
        return True

    def download(url):
        """Process the url and either open a file, or download data.
        Use the token for OSM."""
        pass

    def upload(osc):
        """Uploads the osmChange file."""
        pass

    def refresh_base(data):
        """Downloads all the objects from data."""
        pass


def parse_xml(data):
    pass


def to_osc(data, josm=False):
    pass


def parse_json(data):
    pass
