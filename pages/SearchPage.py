from configs.locators import SearchPageLocators
from utils.classes.Waiter import Waiter
import time


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_show_search_form = self.driver.find_element(*SearchPageLocators.button_show_search_form)
        self.field_search = self.driver.find_element(*SearchPageLocators.field_search)
        self.button_search = self.driver.find_element(*SearchPageLocators.button_search)
        self.waiter = Waiter(self.driver, locator=SearchPageLocators.wrap)

    def __call__(self):
        self.radio_scope_users = self.driver.find_element(*SearchPageLocators.radio_scope_users)

    def fill_field_search(self, value):
        time.sleep(0.5)
        self.field_search.clear()
        self.field_search.send_keys(value)

    def find_user(self, value):
        self.__call__()
        self.button_show_search_form.click()
        self.waiter.wait_attribute_to_be_open()
        self.radio_scope_users.click()
        self.fill_field_search(value)
        self.button_search.click()

    def find_user_basic(self, value):
        self.button_show_search_form.click()
        self.waiter.wait_attribute_to_be_open()
        self.fill_field_search(value)
        self.button_search.click()
