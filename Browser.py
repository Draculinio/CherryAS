import requests
import json


class Browser:
    def __init__(self, host, session_id):
        self.session_id = session_id
        self.host = host


    def maximize(self):
        requests.request('POST', self.host + 'session/' + self.session_id + '/window/maximize')

    def minimize(self):
        requests.request('POST', self.host + 'session/' + self.session_id + '/window/minimize')

    def close_browser(self):
        requests.request('DELETE', self.host + 'session/' + self.session_id + '/window')

    def start_browser(self, capabilities):
        response = requests.request('POST', self.host + 'session', data=json.dumps(capabilities).encode('utf8'))
        return json.loads(response.text)['sessionId'] #TODO: solve this

    def full_screen(self):
        requests.request('POST', self.host + 'session/' + self.session_id + '/window/fullscreen')

    def new_window(self):
        requests.request('POST', self.host + 'session/' + self.session_id + '/window/new')


    # Navigation TODO: See if this goes here or in another class

    def navigate(self, url):
        requests.request('POST', self.host + 'session/' + self.session_id + '/url',
                         data=json.dumps({"url": url}).encode('utf8'))

    def get_url(self):
        response = requests.request('GET', self.host + 'session/' + self.session_id + '/url')
        url = json.loads(response.text)['value']
        return url
