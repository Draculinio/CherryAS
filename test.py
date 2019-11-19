from Driver import *
from Capabilities import *

caps = Capabilities()
caps.add_desired_capability('browserName', 'chrome')
caps.add_chrome_option('binary', "C:\\Program Files (x86)\\Google Chrome\\Application\\chrome.exe")
caps.add_desired_capability('platform', 'ANY')

driver = Driver()
driver.start(caps.capability)
driver.navigate("http://www.duckduckgo.com")
print(driver.get_url())
print(driver.get_title())
driver.fullscreen()
driver.minimize()
driver.maximize()



# Start manipulating elements

#search_input = driver.get_element('xpath', '//*[@id ="search_form_input_homepage"]')
search_input = driver.get_element('id', 'search_form_input_homepage')
search_button = driver.get_element('xpath', '//*[@id ="search_button_homepage"]')
privacy = driver.get_element_by_property('class', 'js-popout-link js-showcase-popout ddgsi ddgsi-down')
#duckduckgo_logo = driver.get_element('link text', 'About DuckDuckGo')
#span = driver.get_element('tag name', 'span')
#driver.click(duckduckgo_logo)
#driver.back()
#driver.click(span)
#driver.back()
driver.write(search_input, 'Draculinio')
driver.click(search_button)
driver.direction('back')
driver.direction('forward')
driver.back()
driver.forward()

driver.refresh()


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
