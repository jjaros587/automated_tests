from configs.locators import CompaniesPageLocators
from selenium.common.exceptions import NoSuchElementException
from pages.BasePage import BasePage


class CompaniesPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.button_add_company = self.driver.find_element(*CompaniesPageLocators.button_add_company)

    def __call__(self):
        self.__init__(self.driver)

    def click_button_button_add_company(self):
        self.button_add_company.click()

    def click_item_country(self, country):
        self.button_add_company.find_element(*self.fill_tuple(CompaniesPageLocators.item_country, country)).click()

    def add_company(self, country):
        self.click_button_button_add_company()
        self.click_item_country(country)

    def delete_company(self, ico):
        try:
            self.driver.find_element(*self.fill_tuple(CompaniesPageLocators.link_delete_company, ico)).click()
            self.driver.find_element(*CompaniesPageLocators.link_delete_permanent).click()
            self.driver.find_element(*CompaniesPageLocators.link_delete_confirm).click()
        except NoSuchElementException:
            return True
        except Exception as e:
            return False
        else:
            return True