from configs.locators import MenuAttendancePageLocators
from utils.classes.Waiter import Waiter
from pages.navigation.MenuMasterPage import MenuMasterPage
from configs.constants import menu


class MenuAttendancePage(MenuMasterPage):
    def __init__(self, driver):
        self.driver = driver
        self.menu = menu['attendance']
        self.main = self.driver.find_element(*self.fill_tuple(MenuAttendancePageLocators.main, self.menu['main']))
        self.waiter = Waiter(self.driver, locator=self.fill_tuple(MenuAttendancePageLocators.main, self.menu['main']))

    def __call__(self):
        self.__init__(self.driver)
        return self

    def start(self):
        self.main.click()
        self.waiter.wait_attribute_to_be_open()

    def click_link_plan(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuAttendancePageLocators.link_plan, self.menu['plan']['link'])).click()
        super().verify_page(self.driver, self.menu['plan'])

    def click_link_closing(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuAttendancePageLocators.link_closing, self.menu['closing']['link'])).click()
        super().verify_page(self.driver, self.menu['closing'])
