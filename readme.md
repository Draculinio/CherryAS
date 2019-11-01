# Cherry

Cherry is a software for web automation.

It is done with a social experiment of creating all the software while filming the complete process
[List (in spanish)](https://www.youtube.com/playlist?list=PLjM3-neCG6qysucDlqDvPWZyomr-lqwBV)

# Installation

Coming soon.

## Usage

```python
import driver

driver.start(capabilities) # starts the browser with capabilities (json)

driver = Driver() #Starts the driver
driver.start(capabilites) # starts the browser with capabilities (json)
driver.navigate("http://www.something.com") # navigates to the target url
search_input = driver.get_element('xpath', 'some_xpath') #Gets the element by xpath
driver.write(search_input, 'something') #writes something in the element
driver.click(search_button) #Clicks the element
driver.close_browser() #Closes the browser
driver.quit() #Quits the driver
```

## Collaboration

Anyone is free to collaborate, to fork and to pull requests. Later we will set rules.

##License:

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)

## Manual

Coming soon.

## Credits

[Created by Pablo Soifer](https://www.youtube.com/user/Draculinio)

## Social media:

[Twitter](https://twitter.com/CherryAS3)