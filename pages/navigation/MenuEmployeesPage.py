from configs.locators import MenuEmployeesPageLocators
from utils.classes.Waiter import Waiter
from pages.navigation.MenuMasterPage import MenuMasterPage
from configs.constants import menu


class MenuEmployeesPage(MenuMasterPage):
    def __init__(self, driver):
        self.driver = driver
        self.menu = menu['employees']
        self.main = self.driver.find_element(*self.fill_tuple(MenuEmployeesPageLocators.main, self.menu['main']))
        self.waiter = Waiter(self.driver, locator=self.fill_tuple(MenuEmployeesPageLocators.main, self.menu['main']))

    def __call__(self):
        self.__init__(self.driver)
        return self

    def start(self):
        self.main.click()
        self.waiter.wait_attribute_to_be_open()

    def click_link_employees(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuEmployeesPageLocators.link_employees, self.menu['employees']['link'])).click()
        super().verify_page(self.driver, self.menu['employees'])

    def click_link_document_definitions(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuEmployeesPageLocators.link_document_definitions, self.menu['documentDefinition']['link'])).click()
        super().verify_page(self.driver, self.menu['documentDefinition'])

    def click_link_changes(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuEmployeesPageLocators.link_changes, self.menu['changes']['link'])).click()
        super().verify_page(self.driver, self.menu['changes'])

    def click_link_changes_new(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuEmployeesPageLocators.link_changes_new, self.menu['changesNew']['link'])).click()
        super().verify_page(self.driver, self.menu['changesNew'])

    def click_link_documents_overview(self):
        self.start()
        self.main.find_element(*self.fill_tuple(MenuEmployeesPageLocators.link_documents_overview, self.menu['documentOverview']['link'])).click()
        super().verify_page(self.driver, self.menu['documentOverview'])
