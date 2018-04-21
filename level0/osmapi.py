import requests
import time

LEVEL0_API = 'http://level0.osmz.ru/console_auth.php'


def authorize():
    """Sends a call to web level0 and waits for a response."""
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


def url_to_api(url):
    pass


def upload(data):
    pass


def parse_xml(data):
    pass


def to_osc(data, josm=False):
    pass


def parse_json(data):
    pass
