from configs.locators import EmployeeCardPageLocators
from pages.BasePage import BasePage


class EmployeeCardPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.link_employements = self.driver.find_element(*EmployeeCardPageLocators.link_employements)

    def __call__(self, screen):
        if screen == "employments":
            self.button_add_employment = self.driver.find_element(*EmployeeCardPageLocators.button_add_employment)

    def click_link_employements(self):
        self.link_employements.click()

    def click_button_add_employment(self):
        self.button_add_employment.click()

    def click_item_company(self, company):
        self.driver.find_element(*self.fill_tuple(EmployeeCardPageLocators.item_company, company)).click()

    def add_employment(self, company):
        self.click_link_employements()
        self("employments")
        self.click_button_add_employment()
        self.click_item_company(company)
