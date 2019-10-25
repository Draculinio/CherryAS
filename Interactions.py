import requests
import json

class Interactions:
    def __init__(self, host, session):
        self.host = host
        self.session = session

    def write(self, element, text):
        requests.request('POST', self.host + 'session/' + self.session + '/element/' + element + '/value',
                         data=json.dumps({'value': [text]}).encode('utf8'))

    def click(self, element):
        requests.request('POST', self.host + 'session/' + self.session + '/element/' + element + '/click',
                         data=json.dumps({'value': 'click'}).encode('utf8'))
