from configs.locators import ChangeEmployment2PageLocators
from utils.utilsTest import select_dropdown_item
from utils.utilsTest import click_radio_by_value


class ChangeEmployment2OthersPage:
    def __init__(self, driver, changes):
        self.driver = driver
        self.changes = changes
        self.button_save_and_continue = self.driver.find_element(*ChangeEmployment2PageLocators.button_save_and_continue)

        if "salary" in self.changes:
            self.field_salary = self.driver.find_element(*ChangeEmployment2PageLocators.field_salary)
            self.radio_salary_type = self.driver.find_elements(*ChangeEmployment2PageLocators.radio_salary_type)
        if "work_position" in self.changes:
            self.dropdown_position = self.driver.find_element(*ChangeEmployment2PageLocators.dropdown_position)
        if "commitment_or_working_hours" in self.changes:
            self.dropdown_shift_type = self.driver.find_element(*ChangeEmployment2PageLocators.dropdown_shift_type)
            self.field_working_hours = self.driver.find_element(*ChangeEmployment2PageLocators.field_working_hours)
        if "organization_unit_cost_center" in self.changes:
            self.dropdown_organization_unit_id = self.driver.find_element(
                *ChangeEmployment2PageLocators.dropdown_organization_unit_id)
        if "other_workplace" in self.changes:
            self.field_other_workplace = self.driver.find_element(*ChangeEmployment2PageLocators.field_other_workplace)
        if "regular_workplace_for_travel_refunds" in self.changes:
            self.field_regular_workplace_for_travel_refunds = self.driver.find_element(
                *ChangeEmployment2PageLocators.field_regular_workplace_for_travel_refunds)
        if "other_agreements" in self.changes:
            self.radio_having_holidays = self.driver.find_elements(*ChangeEmployment2PageLocators.radio_having_holidays)
            self.field_holiday_days_count = self.driver.find_element(*ChangeEmployment2PageLocators.field_holiday_days_count)

    # salary
    def fill_field_salary(self, salary):
        self.field_salary.clear()
        self.field_salary.send_keys(salary)

    def select_radio_salary_typ(self, salary_type):
        click_radio_by_value(self.radio_salary_type, salary_type)

    # work_position
    def fill_dropdown_position(self, position):
        select_dropdown_item(self.dropdown_position, position)

    # commitment_or_working_hours
    def fill_dropdown_shift_type(self, shift_type):
        select_dropdown_item(self.dropdown_shift_type, shift_type)

    def fill_field_working_hours(self, working_hours):
        self.field_working_hours.clear()
        self.field_working_hours.send_keys(working_hours)

    # organization_unit_cost_center
    def fill_dropdown_organization_unit_cost_center(self, organization_unit_id):
        select_dropdown_item(self.dropdown_organization_unit_id, organization_unit_id)

    # other_workplace
    def fill_field_other_workplace(self, other_workplace):
        self.field_other_workplace.clear()
        self.field_other_workplace.send_keys(other_workplace)

    # regular_workplace_for_travel_refunds
    def fill_field_regular_workplace_for_travel_refunds(self, regular_workplace_for_travel_refunds):
        self.field_regular_workplace_for_travel_refunds.clear()
        self.field_regular_workplace_for_travel_refunds.send_keys(regular_workplace_for_travel_refunds)

    # other_agreements
    def select_radio_having_holidays(self, having_holidays):
        click_radio_by_value(self.radio_having_holidays, having_holidays)

    def fill_field_holiday_days_count(self, holiday_days_count):
        self.field_holiday_days_count.clear()
        self.field_holiday_days_count.send_keys(holiday_days_count)
    # --------------------------------------------------------------------------------------------------------------

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, change_employment2):
        if "salary" in self.changes:
            self.fill_field_salary(change_employment2['salary']['salary'])
            self.select_radio_salary_typ(change_employment2['salary']['salary_type'])
        if "work_position" in self.changes:
            self.fill_dropdown_position(change_employment2['work_position']['position'])
        if "commitment_or_working_hours" in self.changes:
            self.fill_dropdown_shift_type(change_employment2['commitment_or_working_hours']['shift_type'])
            self.fill_field_working_hours(change_employment2['commitment_or_working_hours']['working_hours'])
        if "organization_unit_cost_center" in self.changes:
            self.fill_dropdown_organization_unit_cost_center(change_employment2['organization_unit_cost_center']['organization_unit_id'])
        if "other_workplace" in self.changes:
            self.fill_field_other_workplace(change_employment2['other_workplace']['other_workplace'])
        if "regular_workplace_for_travel_refunds" in self.changes:
            self.fill_field_regular_workplace_for_travel_refunds(change_employment2['regular_workplace_for_travel_refunds']['regular_workplace_for_travel_refunds'])
        if "other_agreements" in self.changes:
            self.select_radio_having_holidays(change_employment2['other_agreements']['having_holidays'])
            if change_employment2['other_agreements']['having_holidays'] == "1":
                self.fill_field_holiday_days_count(change_employment2['other_agreements']['holiday_days_count'])
        self.click_button_save_and_continue()

    def test_basic_positive(self, change_employment2):
        self.fill_form(change_employment2)
        if "benefits" in self.changes:
            assert 'benefits' in self.driver.current_url, "Nepodařilo se odeslat 2. část formuláře pro vytvoření dodatku!"
        else:
            assert 'documents-and-evidence' in self.driver.current_url, "Nepodařilo se odeslat 2. část formuláře pro vytvoření dodatku!"

