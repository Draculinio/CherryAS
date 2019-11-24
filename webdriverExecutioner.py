import subprocess


class WebDriverExecutioner:
    def __init__(self):
    #    self.driver_name = driver_name
    #    self.port = port
        self.process = ''

    def launch_driver(self, driver_name='chromedriver', port='9000'):
        my_process = driver_name+'.exe --port='+port
        self.process = subprocess.Popen('chromedriver.exe --port=9000')

    def terminate_driver(self):
        self.process.terminate()

