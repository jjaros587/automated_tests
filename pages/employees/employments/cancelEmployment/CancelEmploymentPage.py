from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from utils.utilsTest import select_dropdown_item
from utils.utilsTest import click_radio_by_value
from selenium.webdriver.common.keys import Keys
import time
from configs.locators import CancelEmploymentPageLocators
from pages.employees.employments.BaseChangePage import BaseChangePage


class CancelEmploymentPage(BaseChangePage):
    leaving_benefit_types = {
        "Žádná odměna": None,
        "Mimořádná odměna": CancelEmploymentPageLocators.field_leaving_benefit_bonus,
        "Odchodné": CancelEmploymentPageLocators.field_leaving_benefit_average_salary_multiplier,
    }

    def __init__(self, driver, employee_isntance):
        super().__init__(driver, employee_isntance)

    def __call__(self):
        self.dropdown_termination_method_identifier = self.driver.find_element(*CancelEmploymentPageLocators.dropdown_termination_method_identifier)
        self.field_termination_notice_delivery_date = self.driver.find_element(*CancelEmploymentPageLocators.field_termination_notice_delivery_date)
        self.field_termination_date = self.driver.find_element(*CancelEmploymentPageLocators.field_termination_date)
        self.dropdown_leaving_benefit_type = self.driver.find_element(*CancelEmploymentPageLocators.dropdown_leaving_benefit_type)
        self.radio_competitive_clause_agreed = self.driver.find_elements(*CancelEmploymentPageLocators.radio_competitive_clause_agreed)
        self.button_save_and_continue = self.driver.find_element(*CancelEmploymentPageLocators.button_save_and_continue)

    def fill_dropdown_termination_method_identifier(self, termination_method_identifier):
        select_dropdown_item(self.dropdown_termination_method_identifier, termination_method_identifier)

    def fill_field_termination_notice_delivery_date(self, termination_notice_delivery_date):
        self.field_termination_notice_delivery_date.clear()
        self.field_termination_notice_delivery_date.send_keys(termination_notice_delivery_date)
        self.field_termination_notice_delivery_date.send_keys(Keys.TAB)

    def fill_field_termination_date(self, termination_notice_delivery_date):
        self.field_termination_date.clear()
        self.field_termination_date.send_keys(termination_notice_delivery_date)
        self.field_termination_date.send_keys(Keys.TAB)

    def fill_dropdown_leaving_benefit_type(self, leaving_benefit_type):
        select_dropdown_item(self.dropdown_leaving_benefit_type, leaving_benefit_type)

    def select_radio_competitive_clause_agreed(self, competitive_clause_agreed):
        time.sleep(0.5)
        click_radio_by_value(self.radio_competitive_clause_agreed, competitive_clause_agreed)

    def fill_field_leaving_benefit(self, option, amount):
        if option not in self.leaving_benefit_types.keys():
            raise ValueError("V testovacích datech je zadána neplatná hodnota parametru leaving_benefit_type: " + option)
        if self.leaving_benefit_types[option] is None:
            return
        element = self.driver.find_element(*self.leaving_benefit_types[option])
        element.clear()
        element.send_keys(amount)

    def fill_field_competitive_clause_months(self, competitive_clause_months):
        element = self.driver.find_element(*CancelEmploymentPageLocators.field_competitive_clause_months)
        element.clear()
        element.send_keys(competitive_clause_months)

    def fill_field_competitive_clause_average_salary_percent(self, competitive_clause_average_salary_percent):
        element = self.driver.find_element(*CancelEmploymentPageLocators.field_competitive_clause_average_salary_percent)
        element.clear()
        element.send_keys(competitive_clause_average_salary_percent)

    def fill_field_competitive_clause_agreements(self, competitive_clause_agreements):
        element = self.driver.find_element(*CancelEmploymentPageLocators.field_competitive_clause_agreements)
        element.clear()
        element.send_keys(competitive_clause_agreements)

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, cancel_employment):
        self.fill_dropdown_termination_method_identifier(cancel_employment['termination_method_identifier'])
        self.fill_field_termination_notice_delivery_date(cancel_employment['termination_notice_delivery_date'])
        self.fill_field_termination_date(cancel_employment['termination_notice_delivery_date'])
        self.fill_dropdown_leaving_benefit_type(cancel_employment['leaving_benefit_type'])
        self.fill_field_leaving_benefit(cancel_employment['leaving_benefit_type'], cancel_employment['leaving_benefit_amount'])
        self.select_radio_competitive_clause_agreed(cancel_employment['competitive_clause_agreed'])
        if cancel_employment['competitive_clause_agreed']:
            self.fill_field_competitive_clause_months(cancel_employment['competitive_clause_months'])
            self.fill_field_competitive_clause_average_salary_percent(cancel_employment['competitive_clause_average_salary_percent'])
            self.fill_field_competitive_clause_agreements(cancel_employment['competitive_clause_agreements'])
        self.click_button_save_and_continue()

    def test_basic_positive(self, company, cancel_employment):
        NewEmploymentMasterPage(self.driver, self.employee_instance).test_basic_positive(company)
        self.go_cancel()
        self()
        self.fill_form(cancel_employment)
        assert 'summary' in self.driver.current_url, "Nepodařilo se odeslat formulář pro zrušení poměru!"
        self.driver.find_element(*CancelEmploymentPageLocators.button_create_termination).click()
        assert 'created' in self.driver.current_url, "Nepodařilo se schválit zrušení poměru!"