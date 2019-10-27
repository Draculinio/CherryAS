import requests
import json
import subprocess
from Driver import *


process = subprocess.Popen('chromedriver.exe --port=9000')

capabilites = {
    "desiredCapabilities":{
        "browserName":"chrome",
        "chromeoptions":{
            "binary":"C:\\Program Files (x86)\\Google Chrome\\Application\\chrome.exe"
        },
        "platform": "ANY"
    }
}

driver = Driver()
driver.start(capabilites)
driver.navigate("http://www.duckduckgo.com")
driver.maximize()
driver.minimize()
driver.fullscreen()

# Start manipulating elements

search_input = driver.get_element('xpath', '//*[@id ="search_form_input_homepage"]')
search_button = driver.get_element('xpath', '//*[@id ="search_button_homepage"]')
driver.write(search_input, 'Draculinio')
driver.click(search_button)

#element = Elements(host, session_id)
#interaction = Interactions(host, session_id)
#search_input = element.get_element('xpath', '//*[@id ="search_form_input_homepage"]')
#search_button = element.get_element('xpath', '//*[@id ="search_button_homepage"]')
#interaction.write(search_input, 'Draculinio')
#interaction.click(search_button)

driver.close_browser()
driver.quit()

process.terminate()

