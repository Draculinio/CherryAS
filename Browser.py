import requests
import json


class Browser:
    def __init__(self, request_url):
        self.request_url = request_url

    def maximize(self):
        '''
        Maximizes the browser
        '''
        print(self.request_url)
        requests.request('POST', self.request_url + '/window/maximize')

    def minimize(self):
        '''
        Minimizes the browser
        '''
        requests.request('POST', self.request_url + '/window/minimize')

    def close_browser(self):
        '''
        Closes the browser
        '''
        requests.request('DELETE', self.request_url  + '/window')

    def full_screen(self):
        '''
        Moves to full screen
        '''
        requests.request('POST', self.request_url + '/window/fullscreen')

    def new_window(self):
        '''
        Opens a new Window
        '''
        requests.request('POST', self.request_url + '/window/new')

    def back(self):
        '''
        Goes Back
        '''
        requests.request('POST', self.request_url + '/back')

    def forward(self):
        '''
        Goes Forward
        '''
        requests.request('POST', self.request_url + '/forward')

    def refresh(self):
        '''
        Refresh the browser
        '''
        requests.request('POST', self.request_url + '/refresh')

    def navigate(self, url):
        '''
        Navigates the browser
        '''
        requests.request('POST', self.request_url + '/url',
                         data=json.dumps({"url": url}).encode('utf8'))

    # Navigation TODO: See if this goes here or in another class

    def get_url(self):
        '''
        Gets the actual URL
        '''
        response = requests.request('GET', self.request_url + '/url')
        return json.loads(response.text)['value']

    def get_title(self):
        '''
        Gets the title of the page
        '''
        response = requests.request('GET', self.request_url + '/title')
        return json.loads(response.text)['value']

    #def start_browser(self, capabilities):
    #    response = requests.request('POST', self.host + 'session', data=json.dumps(capabilities).encode('utf8'))
    #    return json.loads(response.text)['sessionId'] #TODO: NEXT THING TO SOLVE