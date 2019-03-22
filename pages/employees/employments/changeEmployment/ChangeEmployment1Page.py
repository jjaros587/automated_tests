from configs.locators import ChangeEmployment1PageLocators
from utils.utilsTest import click_checkbox_by_value
import copy
from selenium.webdriver.common.keys import Keys


class ChangeEmployment1Page:
    def __init__(self, driver):
        self.driver = driver
        self.field_date_from = self.driver.find_element(*ChangeEmployment1PageLocators.field_date_from)
        self.field_date_to = self.driver.find_element(*ChangeEmployment1PageLocators.field_date_to)
        self.checkbox_change = self.driver.find_elements(*ChangeEmployment1PageLocators.checkbox_change)
        self.button_save_and_continue = self.driver.find_element(*ChangeEmployment1PageLocators.button_save_and_continue)

    def __call__(self):
        self.__init__(self.driver)

    def fill_field_date_from(self, date_from):
        self.field_date_from.clear()
        self.field_date_from.send_keys(date_from)
        self.field_date_from.send_keys(Keys.ENTER)

    def fill_field_date_to(self, date_to):
        self.field_date_to.clear()
        self.field_date_to.send_keys(date_to)
        self.field_date_to.send_keys(Keys.ENTER)

    def fill_change_types(self, changes):
        click_checkbox_by_value(self.checkbox_change, changes, locator="1")

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, change_employment1, changes):
        self.fill_field_date_from(change_employment1['date_from'])
        self.fill_field_date_to(change_employment1['date_to'])
        self.fill_change_types(changes)
        self.click_button_save_and_continue()

    def test_basic_positive(self, change_employment1, changes):
        self.fill_form(change_employment1, changes)
        if len(changes) == 1 and "benefits" in changes:
            assert 'benefits' in self.driver.current_url, "Nepodařilo se odeslat 1. část formuláře pro vytvoření dodatku!"
        else:
            assert 'required-changes' in self.driver.current_url, "Nepodařilo se odeslat 1. část formuláře pro vytvoření dodatku!"


