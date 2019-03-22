from selenium.webdriver.support.events import EventFiringWebDriver
from utils.classes.ScreenshotListener import ScreenshotListener
from pages.login.LoginPage import LoginPage
from tests.SuperTest import SuperTest


class BaseTest(SuperTest):

    def setUp(self):
        self.driver = super().run_driver()
        self.driver = EventFiringWebDriver(self.driver, ScreenshotListener(self._testMethodName))
        LoginPage(self.driver).login_as_super_admin()

    def tearDown(self):
        super().delete_users(self.driver, self.employees)
        super().delete_company(self.driver, self.ico)
        self.driver.quit()
