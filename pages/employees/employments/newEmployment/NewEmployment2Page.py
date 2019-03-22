from configs.locators import NewEmployment2PageLocators
from utils.utilsTest import click_radio_by_value
from utils.utilsTest import select_dropdown_item
from selenium.common.exceptions import TimeoutException
from utils.classes.Waiter import Waiter


class NewEmployment2Page:

    reward_types = {
        "exact-amount": NewEmployment2PageLocators.field_exact_amount,
        "hourly-bonus": NewEmployment2PageLocators.field_hourly_amount,
        "percentual-bonus": NewEmployment2PageLocators.field_percentual_amount
    }

    def __init__(self, driver):
        self.driver = driver
        self.dropdown_duration_months = self.driver.find_element(*NewEmployment2PageLocators.dropdown_duration_months)
        self.dropdown_trial_period_months = self.driver.find_element(*NewEmployment2PageLocators.dropdown_trial_period_months)
        self.dropdown_shift_type = self.driver.find_element(*NewEmployment2PageLocators.dropdown_shift_type)
        self.field_working_hours_per_week = self.driver.find_element(*NewEmployment2PageLocators.field_working_hours_per_week)
        self.radio_working_hours_type = self.driver.find_elements(*NewEmployment2PageLocators.radio_working_hours_type)
        self.link_add_benefits = None
        self.field_basic_salary = self.driver.find_element(*NewEmployment2PageLocators.field_basic_salary)
        self.button_save_and_continue = self.driver.find_element(*NewEmployment2PageLocators.button_save_and_continue)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.dropdown_type_id = self.driver.find_element(*NewEmployment2PageLocators.dropdown_type_id)
        self.button_save = self.driver.find_element(*NewEmployment2PageLocators.button_save)
        self.link_close = self.driver.find_element(*NewEmployment2PageLocators.link_close)

    def fill_dropdown_duration_months(self, duration_months):
        select_dropdown_item(self.dropdown_duration_months, duration_months)

    def fill_dropdown_trial_period_months(self, trial_period_months):
        select_dropdown_item(self.dropdown_trial_period_months, trial_period_months)

    def fill_dropdown_shift_type(self, shift_type):
        select_dropdown_item(self.dropdown_shift_type, shift_type)

    def fill_field_working_hours_per_week(self, working_hours_per_week):
        self.field_working_hours_per_week.clear()
        self.field_working_hours_per_week.send_keys(working_hours_per_week)

    def select_radio_working_hours_type(self, working_hours_type):
        click_radio_by_value(self.radio_working_hours_type, working_hours_type)

    def fill_field_basic_salary(self, basic_salary):
        self.field_basic_salary.clear()
        self.field_basic_salary.send_keys(basic_salary)

    def click_link_add_benefits(self):
        self.link_add_benefits.click()
        self.waiter.wait_for_modal("open")

    # BENEFITS
    def fill_dropdown_type_id(self, type_id):
        select_dropdown_item(self.dropdown_type_id, type_id)

    def fill_field_amount(self, reward_type, amount):
        if reward_type not in self.reward_types.keys():
            raise ValueError("V testovacích datech je zadána neplatná hodnota parametru reward_type: " + reward_type)
        element = self.driver.find_element(*self.reward_types[reward_type])
        element.clear()
        element.send_keys(amount)

    def click_button_save(self):
        self.button_save.click()

    def click_link_close(self):
        self.link_close.click()
        self.waiter.wait_for_modal("close")
    # -------------------------------------------------------------------------------------------------------------

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, employment2):
        self.fill_dropdown_duration_months(employment2['duration_months'])
        self.fill_dropdown_trial_period_months(employment2['trial_period_months'])
        self.fill_dropdown_shift_type(employment2['shift_type'])
        self.fill_field_working_hours_per_week(employment2['working_hours_per_week'])
        self.select_radio_working_hours_type(employment2['working_hours_type'])
        self.fill_field_basic_salary(employment2['basic_salary'])
        if len(employment2['benefits']) > 0:
            self.link_add_benefits = self.driver.find_element(*NewEmployment2PageLocators.link_add_benefits)
            for benefit in employment2['benefits']:
                self.click_link_add_benefits()
                self()
                try:
                    self.fill_dropdown_type_id(benefit['type_id'])
                    self.fill_field_amount(benefit['reward_type'], benefit['amount'])
                except Exception as e:
                    self.click_link_close()
                    assert False, "Nepovedlo se přidat benefit: " + str(e)
                else:
                    self.click_button_save()
                try:
                    self.waiter.wait_for_modal("close")
                except TimeoutException:
                    self()
                    self.click_link_close()
                    assert False, "Nepovedlo se přidat benefit!"
        self.click_button_save_and_continue()

    def test_basic_positive(self, employment2):
        self.fill_form(employment2)
        assert 'other-agreements' in self.driver.current_url, "Nepovedlo se odeslat 2. část formuláře pro vytvoření poměru!"
