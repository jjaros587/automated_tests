from configs.locators import MenuRequestsPageLocators
from pages.navigation.MenuMasterPage import MenuMasterPage
from configs.constants import menu


class MenuRequestsPage(MenuMasterPage):
    def __init__(self, driver):
        self.driver = driver
        self.menu = menu['requests']
        self.main = self.driver.find_element(*self.fill_tuple(MenuRequestsPageLocators.main, self.menu['link']))

    def __call__(self):
        self.__init__(self.driver)
        return self

    def click_approval_requests(self):
        self.main.click()
        super().verify_page(self.driver, self.menu)
