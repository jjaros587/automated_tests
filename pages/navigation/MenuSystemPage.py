from configs.locators import MenuSystemPageLocators
from utils.classes.Waiter import Waiter
from pages.navigation.MenuMasterPage import MenuMasterPage
from configs.constants import menu


class MenuSystemPage(MenuMasterPage):
    def __init__(self, driver):
        self.driver = driver
        self.menu = menu['system']
        self.waiter = Waiter(self.driver, locator=self.fill_tuple(MenuSystemPageLocators.main, self.menu['main']))
        self.main = self.driver.find_element(*self.fill_tuple(MenuSystemPageLocators.main, self.menu['main']))

    def __call__(self):
        self.__init__(self.driver)
        return self

    def start(self):
        self.main.click()
        self.waiter.wait_attribute_to_be_open()

    def click_link_users(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuSystemPageLocators.link_users, self.menu['users']['link'])).click()
        super().verify_page(self.driver, self.menu['users'])

    def click_link_roles(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuSystemPageLocators.link_roles, self.menu['roles']['link'])).click()
        super().verify_page(self.driver, self.menu['roles'])

    def click_link_companies(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuSystemPageLocators.link_companies, self.menu['companies']['link'])).click()
        super().verify_page(self.driver, self.menu['companies'])

    def click_link_system_settings(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuSystemPageLocators.link_system_settings, self.menu['systemSettings']['link'])).click()
        super().verify_page(self.driver, self.menu['systemSettings'])

    def click_link_licence(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuSystemPageLocators.link_licence, self.menu['licence']['link'])).click()
        super().verify_page(self.driver, self.menu['licence'])


