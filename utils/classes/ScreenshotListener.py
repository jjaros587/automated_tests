from selenium.webdriver.support.events import AbstractEventListener
import os
from configs.config import folders


class ScreenshotListener(AbstractEventListener):
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def on_exception(self, exception, driver):
        path = folders['screenshots'] + os.environ.get('BROWSER') + '/'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        driver.get_screenshot_as_file(path + "screenshot_" + os.environ.get('BROWSER') + "'%s'.png" % self.test_method_name)