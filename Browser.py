import requests
import json


class Browser:
    def __init__(self, request_url):
        self.request_url = request_url

    def maximize(self):
        print(self.request_url)
        requests.request('POST', self.request_url + '/window/maximize')

    def minimize(self):
        requests.request('POST', self.request_url + '/window/minimize')

    def close_browser(self):
        requests.request('DELETE', self.request_url  + '/window')

    def full_screen(self):
        requests.request('POST', self.request_url + '/window/fullscreen')

    def new_window(self):
        requests.request('POST', self.request_url + '/window/new')

    def back(self):
        requests.request('POST', self.request_url + '/back')

    def forward(self):
        requests.request('POST', self.request_url + '/forward')

    def refresh(self):
        requests.request('POST', self.request_url + '/refresh')

    def navigate(self, url):
        requests.request('POST', self.request_url + '/url',
                         data=json.dumps({"url": url}).encode('utf8'))

    # Navigation TODO: See if this goes here or in another class

    def get_url(self):
        response = requests.request('GET', self.request_url + '/url')
        return json.loads(response.text)['value']

    def get_title(self):
        response = requests.request('GET', self.request_url + '/title')
        return json.loads(response.text)['value']

    #def start_browser(self, capabilities):
    #    response = requests.request('POST', self.host + 'session', data=json.dumps(capabilities).encode('utf8'))
    #    return json.loads(response.text)['sessionId'] #TODO: NEXT THING TO SOLVE