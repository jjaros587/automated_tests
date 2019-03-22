from configs.locators import PersonalInquiry3PageLocators
from utils.utilsTest import click_radio_by_value
from utils.utilsTest import select_dropdown_item
from pages.BasePage import BasePage


class PersonalInquiry3Page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.field_paycheck_password = self.driver.find_element(*PersonalInquiry3PageLocators.field_paycheck_password)
        self.dropdown_health_insurance_company_code = self.driver.find_element(*PersonalInquiry3PageLocators.dropdown_health_insurance_company_code)
        self.radio_having_some_pension = self.driver.find_elements(*PersonalInquiry3PageLocators.radio_having_some_pension)
        self.radio_having_handicap_or_disability_card = self.driver.find_elements(*PersonalInquiry3PageLocators.radio_having_handicap_or_disability_card)
        self.radio_having_wages_deductions = self.driver.find_elements(*PersonalInquiry3PageLocators.radio_having_wages_deductions)
        self.radio_having_social_insurance_abroad = self.driver.find_elements(*PersonalInquiry3PageLocators.radio_having_social_insurance_abroad)
        self.button_save_and_recap = self.driver.find_element(*PersonalInquiry3PageLocators.button_save_and_recap)

    def __call__(self):
        self.__init__(self.driver)

    def fill_field_heslo_paska(self, paycheck_password):
        self.field_paycheck_password.clear()
        self.field_paycheck_password.send_keys(paycheck_password)

    def fill_dropdown_health_insurance_company_code(self, health_insurance_company_code):
        select_dropdown_item(self.dropdown_health_insurance_company_code, health_insurance_company_code, "known")

    def select_radio_having_some_pension(self, having_some_pension):
        click_radio_by_value(self.radio_having_some_pension, having_some_pension)

    def select_radio_having_handicap_or_disability_card(self, having_handicap_or_disability_card):
        click_radio_by_value(self.radio_having_handicap_or_disability_card, having_handicap_or_disability_card)

    def select_radio_having_wages_deductions(self, having_wages_deductions):
        click_radio_by_value(self.radio_having_wages_deductions, having_wages_deductions)

    def select_having_social_insurance_abroad(self, having_social_insurance_abroad):
        click_radio_by_value(self.radio_having_social_insurance_abroad, having_social_insurance_abroad)

    def click_button_save_and_recap(self):
        self.button_save_and_recap.click()

    def fill_form(self, inquiry3):
        self.fill_field_heslo_paska(inquiry3['paycheck_password'])
        self.fill_dropdown_health_insurance_company_code(inquiry3['health_insurance_company_code'])
        self.select_radio_having_some_pension(inquiry3['having_some_pension'])
        self.select_radio_having_handicap_or_disability_card(inquiry3['having_handicap_or_disability_card'])
        self.select_radio_having_wages_deductions(inquiry3['having_wages_deductions'])
        self.select_having_social_insurance_abroad(inquiry3['having_social_insurance_abroad'])
        self.click_button_save_and_recap()

    def test_basic_positive(self, inquiry3):
        self.fill_form(inquiry3)
        assert self.screens['inquiry']['summary'] in self.driver.current_url, "3. část formuláře osobního dotazníku se nepodařilo odeslat!"

