import requests
from Interactions import *
from Elements import *
from Browser import *
from webdriverExecutioner import *


class Driver:
    def __init__(self):
        self.host = ''
        self.session_id = ''
        self.interactions = ''
        self.elements = ''
        self.browser = ''
        self.webdriver_exec = WebDriverExecutioner()
        self.request_url = ''

    def start(self, capabilities, host='http://127.0.0.1:9000/'):
        self.webdriver_exec.launch_driver()
        self.host = host
        response = requests.request('POST', self.host + 'session', data=json.dumps(capabilities).encode('utf8'))
        self.session_id = json.loads(response.text)['sessionId'] #Todo: see if session_id variable is necesary
        self.request_url = self.host + 'session/' + self.session_id
        self.interactions = Interactions(self.host, self.session_id)
        self.elements = Elements(self.host, self.session_id)
        self.browser = Browser(self.request_url)

    def close_browser(self):
        self.browser.close_browser()

    def get_element(self, locator, value):
        return self.elements.get_element(locator, value)

    def click(self, element):
        self.interactions.click(element)

    def write(self, element, text):
        self.interactions.write(element, text)

    def navigate(self, url):
        self.browser.navigate(url)

    def quit(self):
        requests.request('DELETE', self.host + 'session/' + self.session_id)
        self.webdriver_exec.terminate_driver()

    def maximize(self):
        self.browser.maximize()

    def minimize(self):
        self.browser.minimize()

    def fullscreen(self):
        self.browser.full_screen()

    def new_window(self):
        self.browser.new_window()

    def get_url(self):
        return self.browser.get_url()

    def get_title(self):
        return self.browser.get_title()

    def direction(self, direction):
        if direction.upper() == 'BACK':
            self.browser.back()
        else:
            self.browser.forward()

    def back(self):
        self.browser.back()

    def forward(self):
        self.browser.forward()

    def refresh(self):
        self.browser.refresh()

    def get_element_by_property(self, prop, value):
        value = '//*[@' + prop + ' ="' + value + '"]'
        return self.elements.get_element('xpath', value)

    def get_element_by_id(self, value):
        value = '//*[@id ="'+value+'"]'
        return self.elements.get_element('xpath', value)

    def get_element_by_xpath(self, value):
        return self.elements.get_element('xpath', value)

    def get_element_by_link_text(self,value):
        return self.elements.get_element('link text', value)

    def get_element_by_css(self,value):
        return self.elements.get_element('css selector', value)

    def get_element_by_partial_link_text(self,value):
        return self.elements.get_element('partial link text', value)

    def get_element_by_tag(self,value):
        return self.elements.get_element('tag name', value)
