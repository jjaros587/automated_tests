from configs.locators import NewCompany1PageLocators
from utils.utilsTest import select_dropdown_item
from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage
import time


class NewCompany1Page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.field_name = self.driver.find_element(*NewCompany1PageLocators.field_name)
        self.field_shortened_name = self.driver.find_element(*NewCompany1PageLocators.field_shortened_name)
        self.field_identification_code = self.driver.find_element(*NewCompany1PageLocators.field_identification_code)
        self.field_address_street_and_number = self.driver.find_element(*NewCompany1PageLocators.field_address_street_and_number)
        self.field_address_city = self.driver.find_element(*NewCompany1PageLocators.field_address_city)
        self.dropdown_address_zip = self.driver.find_element(*NewCompany1PageLocators.dropdown_address_zip)
        self.field_registered_when = self.driver.find_element(*NewCompany1PageLocators.field_registered_when)
        self.field_court_name = self.driver.find_element(*NewCompany1PageLocators.field_court_name)
        self.field_court_case = self.driver.find_element(*NewCompany1PageLocators.field_court_case)
        self.field_default_wages_item_code = self.driver.find_element(*NewCompany1PageLocators.field_default_wages_item_code)
        self.field_wages_constant_symbol = self.driver.find_element(*NewCompany1PageLocators.field_wages_constant_symbol)
        self.dropdown_wages_variable_symbol_strategy = self.driver.find_element(*NewCompany1PageLocators.dropdown_wages_variable_symbol_strategy)
        self.button_save_and_continue = self.driver.find_element(*NewCompany1PageLocators.button_save_and_continue)
        self.button_load_automatically = self.driver.find_element(*NewCompany1PageLocators.button_load_automatically)

    def __call__(self):
        self.__init__(self.driver)

    def fill_field_name(self, name):
        time.sleep(1)
        self.field_name.clear()
        self.field_name.send_keys(name)

    def fill_field_shortened_name(self, shortened_name):
        self.field_shortened_name.clear()
        self.field_shortened_name.send_keys(shortened_name)

    def fill_field_identification_code(self, identification_code):
        self.field_identification_code.clear()
        self.field_identification_code.send_keys(identification_code)

    def fill_field_address_street_and_number(self, address_street_and_number):
        self.field_address_street_and_number.clear()
        self.field_address_street_and_number.send_keys(address_street_and_number)

    def fill_field_address_city(self, address_city):
        self.field_address_city.clear()
        self.field_address_city.send_keys(address_city)

    def fill_dropdown_address_zip(self, address_zip):
        select_dropdown_item(self.dropdown_address_zip, address_zip)

    def fill_field_registered_when(self, registered_when):
        self.field_registered_when.clear()
        self.field_registered_when.send_keys(registered_when)
        self.field_registered_when.send_keys(Keys.ENTER)

    def fill_field_court_name(self, court_name):
        self.field_court_name.clear()
        self.field_court_name.send_keys(court_name)

    def fill_field_court_case(self, court_case):
        self.field_court_case.clear()
        self.field_court_case.send_keys(court_case)

    def fill_field_default_wages_item_code(self, default_wages_item_code):
        self.field_default_wages_item_code.clear()
        self.field_default_wages_item_code.send_keys(default_wages_item_code)

    def fill_field_wages_constant_symbol(self, wages_constant_symbol):
        self.field_wages_constant_symbol.clear()
        self.field_wages_constant_symbol.send_keys(wages_constant_symbol)

    def fill_dropdown_wages_variable_symbol_strategy(self, wages_variable_symbol_strategy):
        select_dropdown_item(self.dropdown_wages_variable_symbol_strategy, wages_variable_symbol_strategy)

    def click_button_save_and_continue(self):
        time.sleep(0.5)
        self.button_save_and_continue.click()

    def click_button_load_automatically(self):
        self.button_load_automatically.click()
        while self.driver.execute_script("return $.active") != 0:
            pass

    def fill_form_automatically(self, company1):
        self.fill_field_shortened_name(company1['shortened_name'])
        self.fill_field_identification_code(company1['identification_code'])
        self.click_button_load_automatically()
        self.fill_field_default_wages_item_code(company1['default_wages_item_code'])
        self.fill_field_wages_constant_symbol(company1['wages_constant_symbol'])
        self.fill_dropdown_wages_variable_symbol_strategy(company1['wages_variable_symbol_strategy'])
        self.click_button_save_and_continue()

    def fill_form(self, company1):
        self.fill_field_shortened_name(company1['shortened_name'])
        self.fill_field_identification_code(company1['identification_code'])
        self.fill_field_address_street_and_number(company1['address_street_and_number'])
        self.fill_field_address_city(company1['address_city'])
        self.fill_dropdown_address_zip(company1['address_zip'])
        self.fill_field_registered_when(company1['registered_when'])
        self.fill_field_court_name(company1['court_name'])
        self.fill_field_court_case(company1['court_case'])
        self.fill_field_default_wages_item_code(company1['default_wages_item_code'])
        self.fill_field_wages_constant_symbol(company1['wages_constant_symbol'])
        self.fill_dropdown_wages_variable_symbol_strategy(company1['wages_variable_symbol_strategy'])
        self.fill_field_name(company1['name'])
        self.click_button_save_and_continue()

    def test_basic_positive(self, automatically, company1):
        if automatically:
            self.fill_form_automatically(company1)
        else:
            self.fill_form(company1)
        assert self.screens['company']["2"] in self.driver.current_url, "Nepovedlo se odeslat 1. část formuláře pro vytvoření nové společnosti!"
