import requests
from Interactions import *
from Elements import *
from Browser import *

class Driver:
    def __init__(self):
        self.host = ''
        self.session_id = ''
        self.interactions = ''
        self.elements = ''
        self.browser = ''

    def start(self, capabilities, host='http://127.0.0.1:9000/'):
        self.host = host
        #print(self.browser.start_browser(capabilities))
        response = requests.request('POST', self.host + 'session', data=json.dumps(capabilities).encode('utf8'))
        self.session_id = json.loads(response.text)['sessionId']

        #self.session_id = self.browser.start_browser(capabilities)
        self.interactions = Interactions(self.host, self.session_id)
        self.elements = Elements(self.host, self.session_id)
        self.browser = Browser(self.host, self.session_id)

    def close_browser(self):
        self.browser.close_browser()
        #requests.request('DELETE', self.host + 'session/' + self.session_id + '/window')

    def get_element(self, locator, value):
        return self.elements.get_element(locator, value)

    def click(self, element):
        self.interactions.click(element)

    def write(self, element, text):
        self.interactions.write(element, text)

    def navigate(self, url):
        requests.request('POST', self.host + 'session/' + self.session_id + '/url',
                         data=json.dumps({"url": url}).encode('utf8'))

    def quit(self):
        requests.request('DELETE', self.host + 'session/' + self.session_id)

    def maximize(self):
        self.browser.maximize()

    def minimize(self):
        self.browser.minimize()

    def fullscreen(self):
        self.browser.full_screen()