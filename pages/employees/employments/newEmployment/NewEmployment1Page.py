from configs.locators import NewEmployment1PageLocators
from utils.utilsTest import select_dropdown_item
from utils.utilsTest import click_radio_by_value
from selenium.webdriver.common.keys import Keys
import time


class NewEmployment1Page:
    def __init__(self, driver):
        self.driver = driver
        self.employment_number = self.driver.find_element(*NewEmployment1PageLocators.employment_number).text
        self.radio_type = self.driver.find_elements(*NewEmployment1PageLocators.radio_type)
        self.field_start_date = self.driver.find_element(*NewEmployment1PageLocators.field_start_date)
        self.filed_boarding_date = self.driver.find_element(*NewEmployment1PageLocators.filed_boarding_date)
        self.dropdown_organization_unit_id = self.driver.find_element(*NewEmployment1PageLocators.dropdown_organization_unit_id)
        self.dropdown_cost_center_id = self.driver.find_element(*NewEmployment1PageLocators.dropdown_cost_center_id)
        self.dropdown_work_position_id = self.driver.find_element(*NewEmployment1PageLocators.dropdown_work_position_id)
        self.button_save_and_continue = self.driver.find_element(*NewEmployment1PageLocators.button_save_and_continue)

    def __call__(self):
        self.__init__(self.driver)

    def select_radio_type(self, type):
        click_radio_by_value(self.radio_type, type)

    def fill_field_start_date(self, start_date):
        self.field_start_date.clear()
        self.field_start_date.send_keys(start_date)
        self.field_start_date.send_keys(Keys.ENTER)

    def fill_filed_boarding_date(self, boarding_date):
        self.filed_boarding_date.clear()
        self.filed_boarding_date.send_keys(boarding_date)
        self.filed_boarding_date.send_keys(Keys.ENTER)

    def fill_dropdown_organization_unit_id(self, organization_unit_id):
        select_dropdown_item(self.dropdown_organization_unit_id, organization_unit_id)
        time.sleep(0.25)

    def fill_dropdown_cost_center_id(self, cost_center_id):
        select_dropdown_item(self.dropdown_cost_center_id, cost_center_id)

    def fill_dropdown_work_position_id(self, work_position_id):
        select_dropdown_item(self.dropdown_work_position_id, work_position_id)

    def fill_dropdown_immediate_superior_user_id(self, immediate_superior_user_id):
        time.sleep(0.5)
        element = self.driver.find_element(*NewEmployment1PageLocators.dropdown_immediate_superior_user_id)
        select_dropdown_item(element, immediate_superior_user_id)

    def fill_dropdown_current_approver_id(self, current_approver_id):
        time.sleep(0.25)
        element = self.driver.find_element(*NewEmployment1PageLocators.dropdown_current_approver_id)
        select_dropdown_item(element, current_approver_id)

    def fill_dropdown_superior_of_unit_ids(self, superior_of_unit_ids):
        time.sleep(1)
        element = self.driver.find_element(*NewEmployment1PageLocators.dropdown_superior_of_unit_ids)
        select_dropdown_item(element, superior_of_unit_ids)

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, employment1, employee_instance):
        employee_instance.set_id_employment(self.employment_number)
        self.select_radio_type(employment1['type'])
        self.fill_field_start_date(employment1['start_date'])
        self.fill_filed_boarding_date(employment1['boarding_date'])
        self.fill_dropdown_organization_unit_id(employment1['organization_unit_id'])
        self.fill_dropdown_cost_center_id(employment1['cost_center_id'])
        self.fill_dropdown_work_position_id(employment1['work_position_id'])
        self.fill_dropdown_superior_of_unit_ids(employment1['superior_of_unit_ids'])
        self.fill_dropdown_immediate_superior_user_id(employment1['immediate_superior_user_id'])
        self.fill_dropdown_current_approver_id(employment1['current_approver_id'])

        self.click_button_save_and_continue()

    def test_basic_positive(self, employment1, employee_instance):
        self.fill_form(employment1, employee_instance)
        assert 'duration-and-wage' in self.driver.current_url, "Nepovedlo se odeslat 1. část formuláře pro vytvoření poměru!"

