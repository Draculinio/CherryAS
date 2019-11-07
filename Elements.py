import requests
import json

class Elements:
    def __init__(self, host, session):
        self.host = host
        self.session = session

    def get_element(self, locator, value):
        if locator.upper() == 'ID':
            locator = 'xpath'
            value = '//*[@id ="'+value+'"]'
        if locator.upper() == 'NAME':
            locator = 'xpath'
            value = '//*[@name ="'+value+'"]'
        element = requests.request('POST', self.host + 'session/' + self.session + '/element', data=json.dumps(
            {'using': locator, 'value': value}).encode('utf8'))
        return json.loads(element.text)['value']['ELEMENT']

    def get_element_by_property(self, prop, value):
        value = '//*[@'+prop+' ="' + value + '"]'
        element = requests.request('POST', self.host + 'session/' + self.session + '/element', data=json.dumps(
            {'using': 'xpath', 'value': value}).encode('utf8'))
        return json.loads(element.text)['value']['ELEMENT']

