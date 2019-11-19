#capabilites = {
#    "desiredCapabilities":{
#        "browserName":"chrome",
#        "chromeoptions":{
#            "binary":"C:\\Program Files (x86)\\Google Chrome\\Application\\chrome.exe"
#        },
#        "platform": "ANY"
#    }
#}

from Capabilities import *

caps = Capabilities()
caps.add_desired_capability('browserName', 'chrome')
caps.add_chrome_option('binary', "C:\\Program Files (x86)\\Google Chrome\\Application\\chrome.exe")
caps.add_desired_capability('platform', 'ANY')
print(caps.capability)
