import requests

class Driver:
    def __init__(self,host,session):
        self.host = host
        self.session = session

    def close_browser(self):
        requests.request('DELETE', self.host + 'session/' + self.session + '/window')
