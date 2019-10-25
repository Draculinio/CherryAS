import requests
import json
import subprocess
from Elements import *
from Interactions import *
from Driver import *



process = subprocess.Popen('chromedriver.exe --port=9000')
host = 'http://127.0.0.1:9000/'

capabilites = {
    "desiredCapabilities":{
        "browserName":"chrome",
        "chromeoptions":{
            "binary":"C:\\Program Files (x86)\\Google Chrome\\Application\\chrome.exe"
        },
        "platform": "ANY"
    }
}

response = requests.request('POST', host+'session', data=json.dumps(capabilites).encode('utf8'))
session_id = json.loads(response.text)['sessionId']

element = Elements(host, session_id)
interaction = Interactions(host, session_id)
driver = Driver()


requests.request('POST', host+'session/'+session_id+'/url', data=json.dumps({"url": "http://www.duckduckgo.com"}).encode('utf8'))

# Start manipulating elements
search_input = element.get_element('xpath', '//*[@id ="search_form_input_homepage"]')
search_button = element.get_element('xpath', '//*[@id ="search_button_homepage"]')

interaction.write(search_input, 'Draculinio')
interaction.click(search_button)

driver.close_browser()

requests.request('DELETE', host+'session/'+session_id)
process.terminate()

