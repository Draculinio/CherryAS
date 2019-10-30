import requests
import json
import subprocess
from Driver import *


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
print(driver.get_url())
driver.fullscreen()
driver.minimize()
driver.maximize()



# Start manipulating elements

search_input = driver.get_element('xpath', '//*[@id ="search_form_input_homepage"]')
search_button = driver.get_element('xpath', '//*[@id ="search_button_homepage"]')
driver.write(search_input, 'Draculinio')
driver.click(search_button)


#Legacy (it works but not recomended)
#driver.new_window()
#element = Elements(host, session_id)
#interaction = Interactions(host, session_id)
#search_input = element.get_element('xpath', '//*[@id ="search_form_input_homepage"]')
#search_button = element.get_element('xpath', '//*[@id ="search_button_homepage"]')
#interaction.write(search_input, 'Draculinio')
#interaction.click(search_button)

driver.close_browser()
driver.quit()


