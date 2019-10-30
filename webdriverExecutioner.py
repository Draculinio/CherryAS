import subprocess


class WebDriverExecutioner:
    def __init__(self, driver_name='chromedriver', port=9000):
        self.driver_name = driver_name
        self.port = port
        self.process = ''

    def launch_driver(self):
        self.process = subprocess.Popen('chromedriver.exe --port=9000')

    def terminate_driver(self):
        self.process.terminate()

