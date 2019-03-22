from configs.locators import PersonalInquiry1PageLocators
from utils.utilsTest import element_exists
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class PersonalInquiry1Page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.field_birth_number = self.driver.find_element(*PersonalInquiry1PageLocators.field_birth_number)
        self.field_residence_street_and_house_number = self.driver.find_element(*PersonalInquiry1PageLocators.field_residence_street_and_house_number)
        self.field_residence_city = self.driver.find_element(*PersonalInquiry1PageLocators.field_residence_city)
        self.field_residence_zip = self.driver.find_element(*PersonalInquiry1PageLocators.field_residence_zip)
        self.button_save_and_continue = self.driver.find_element(*PersonalInquiry1PageLocators.button_save_and_continue)

    def __call__(self):
        self.__init__(self.driver)

    def fill_field_birth_number(self, birth_number):
        self.field_birth_number.clear()
        self.field_birth_number.send_keys(birth_number)

    def fill_field_residence_street_and_house_number(self, residence_street_and_house_number):
        self.field_residence_street_and_house_number.clear()
        self.field_residence_street_and_house_number.send_keys(residence_street_and_house_number)

    def fill_field_residence_city(self, residence_city):
        self.field_residence_city.clear()
        self.field_residence_city.send_keys(residence_city)

    def fill_field_residence_zip(self, residence_zip):
        self.field_residence_zip.clear()
        self.field_residence_zip.send_keys(residence_zip)

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, inquiry1):
        self.fill_field_birth_number(inquiry1['birth_number'])
        self.fill_field_residence_street_and_house_number(inquiry1['residence_street_and_house_number'])
        self.fill_field_residence_city(inquiry1['residence_city'])
        self.fill_field_residence_zip(inquiry1['residence_zip'])
        self.click_button_save_and_continue()

    def test_basic_positive(self, inquiry1):
        self.fill_form(inquiry1)
        assert self.screens['inquiry']['2'] in self.driver.current_url, "1. část formuláře osobního dotazníku se nepodařilo odeslat!"

    def test_negative_empty_fields(self, inquiry1, error):
        self.fill_form(inquiry1)
        assert self.screens['inquiry']['2'] not in self.driver.current_url, "1. část formuláře osobního dotazníku se podařilo odeslat s chybami!"
        assert element_exists(self.driver, (By.ID, error)), "Nebyla zobrazena chybová hláška '%s'!" % error
