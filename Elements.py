import requests
import json

class Elements:
    def __init__(self, host, session):
        self.host = host
        self.session = session

    def get_element(self, locator, value):
        element = requests.request('POST', self.host + 'session/' + self.session + '/element', data=json.dumps(
            {'using': locator, 'value': value}).encode('utf8'))
        return json.loads(element.text)['value']['ELEMENT']