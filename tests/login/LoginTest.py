from tests.BaseTest import BaseTest
from pages.login.LoginPage import LoginPage
from configs.constants import dataPath
from ddt import ddt, file_data
from utils.classes.ScreenshotListener import ScreenshotListener
from selenium.webdriver.support.events import EventFiringWebDriver


@ddt
class LogInTest(BaseTest):
    path = dataPath + "login\\"

    def setUp(self):
        self.driver = super().run_driver()
        self.driver = EventFiringWebDriver(self.driver, ScreenshotListener(self._testMethodName))

    @file_data(path + "login_positive.json")
    def test_login_positive(self, username, password):
        LoginPage(self.driver).test_basic_positive(username, password)

    @file_data(path + "login_negative.json")
    def test_login_negative(self, username, password):
        LoginPage(self.driver).test_basic_negative(username, password)
