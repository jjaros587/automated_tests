from configs.locators import PersonalInquiry2PageLocators
from pages.BasePage import BasePage


class PersonalInquiry2Page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.field_birth_place = self.driver.find_element(*PersonalInquiry2PageLocators.field_birth_place)
        self.button_save_and_continue = self.driver.find_element(*PersonalInquiry2PageLocators.button_save_and_continue)

    def __call__(self):
        self.__init__(self.driver)

    def fill_field_birth_place(self, birth_place):
        self.field_birth_place.clear()
        self.field_birth_place.send_keys(birth_place)

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, inquiry2):
        self.fill_field_birth_place(inquiry2['birth_place'])
        self.click_button_save_and_continue()

    def test_basic_positive(self, inquiry2):
        self.fill_form(inquiry2)
        assert self.screens['inquiry']['3'] in self.driver.current_url, "2. část formuláře osobního dotazníku se nepodařilo odeslat!"

