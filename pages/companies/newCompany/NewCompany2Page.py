from configs.locators import NewCompany2PageLocators
from selenium.webdriver.common.keys import Keys
from utils.utilsTest import click_radio_by_value
from utils.utilsTest import select_dropdown_item
from selenium.common.exceptions import TimeoutException
import time
from utils.classes.Waiter import Waiter
from pages.BasePage import BasePage


class NewCompany2Page(BasePage):

    reward_types = {
        "exact-amount": NewCompany2PageLocators.field_exact_amount,
        "hourly-bonus": NewCompany2PageLocators.field_hourly_amount,
        "percentual-bonus": NewCompany2PageLocators.field_percentual_amount
    }

    def __init__(self, driver):
        self.driver = driver
        self.radio_personal_number_format = self.driver.find_elements(*NewCompany2PageLocators.radio_personal_number_format)
        self.radio_personal_number_editable = self.driver.find_elements(*NewCompany2PageLocators.radio_personal_number_editable)
        self.field_minimal_personal_number = self.driver.find_element(*NewCompany2PageLocators.field_minimal_personal_number)
        self.field_balancing_period = self.driver.find_element(*NewCompany2PageLocators.field_balancing_period)
        self.radio_balancing_period_units = self.driver.find_elements(*NewCompany2PageLocators.radio_balancing_period_units)
        self.field_balancing_period_starts_when = self.driver.find_element(*NewCompany2PageLocators.field_balancing_period_starts_when)
        self.radio_having_benefits = self.driver.find_elements(*NewCompany2PageLocators.radio_having_benefits)
        self.link_add_benefits = self.driver.find_element(*NewCompany2PageLocators.link_add_benefits)
        self.button_save_and_continue = self.driver.find_element(*NewCompany2PageLocators.button_save_and_continue)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.driver = self.driver
        self.field_name = self.driver.find_element(*NewCompany2PageLocators.field_name)
        self.field_localized_name_cs = self.driver.find_element(*NewCompany2PageLocators.field_localized_name_cs)
        self.field_localized_name_en = self.driver.find_element(*NewCompany2PageLocators.field_localized_name_en)
        self.field_wage_item_code = self.driver.find_element(*NewCompany2PageLocators.field_wage_item_code)
        self.dropdown_reward_type = self.driver.find_element(*NewCompany2PageLocators.dropdown_reward_type)
        self.field_exact_amount = self.driver.find_element(*NewCompany2PageLocators.field_exact_amount)
        self.radio_for_all_organization_units = self.driver.find_elements(*NewCompany2PageLocators.radio_for_all_organization_units)
        self.radio_for_all_work_positions = self.driver.find_elements(*NewCompany2PageLocators.radio_for_all_work_positions)
        self.button_save = self.driver.find_element(*NewCompany2PageLocators.button_save)
        self.link_close = self.driver.find_element(*NewCompany2PageLocators.link_close)

    def select_radio_personal_number_format(self, os_format):
        click_radio_by_value(self.radio_personal_number_format, os_format)

    def select_radio_personal_number_editable(self, os_editable):
        click_radio_by_value(self.radio_personal_number_editable, os_editable)

    def fill_field_minimal_personal_number(self, os_min):
        self.field_minimal_personal_number.clear()
        self.field_minimal_personal_number.send_keys(os_min)

    def fill_field_balancing_period(self, balancing_period):
        self.field_balancing_period.clear()
        self.field_balancing_period.send_keys(balancing_period)

    def select_radio_balancing_period_units(self, balancing_period_units):
        click_radio_by_value(self.radio_balancing_period_units, balancing_period_units)

    def fill_field_balancing_period_starts_when(self, balancing_period_starts_when):
        self.field_balancing_period_starts_when.clear()
        self.field_balancing_period_starts_when.send_keys(balancing_period_starts_when)
        self.field_balancing_period_starts_when.send_keys(Keys.ENTER)

    def select_radio_having_benefits(self, benefits):
        value = "0" if len(benefits) == 0 else "1"
        click_radio_by_value(self.radio_having_benefits, value)

    def click_link_add_benefits(self):
        time.sleep(0.5)
        self.link_add_benefits.click()
        self.waiter.wait_for_modal("open")

        # BENEFITS
    def fill_field_name(self, name):
        self.field_name.clear()
        self.field_name.send_keys(name)

    def fill_field_localized_name_cs(self, localized_name_cs):
        self.field_localized_name_cs.clear()
        self.field_localized_name_cs.send_keys(localized_name_cs)

    def fill_field_localized_name_en(self, localized_name_en):
        self.field_localized_name_en.clear()
        self.field_localized_name_en.send_keys(localized_name_en)

    def fill_field_wage_item_code(self, wage_item_code):
        self.field_wage_item_code.clear()
        self.field_wage_item_code.send_keys(wage_item_code)

    def fill_dropdown_reward_type(self, reward_type):
        select_dropdown_item(self.dropdown_reward_type, reward_type, "known")

    def fill_field_amount(self, reward_type, amount):
        if reward_type not in self.reward_types.keys():
            raise ValueError("V testovacích datech je zadána neplatná hodnota parametru reward_type: " + reward_type)
        element = self.driver.find_element(*self.reward_types[reward_type])
        element.clear()
        element.send_keys(amount)

    def select_radio_for_all_organization_units(self, for_all_organization_units):
        click_radio_by_value(self.radio_for_all_organization_units, for_all_organization_units)

    def select_radio_for_all_work_positions(self, for_all_work_positions):
        click_radio_by_value(self.radio_for_all_work_positions, for_all_work_positions)

    def click_button_save(self):
        self.button_save.click()

    def click_link_close(self):
        self.link_close.click()
        self.waiter.wait_for_modal("close")
    # --------------------------------------------------------------------------------------------------------------

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, company2):
        self.fill_field_balancing_period(company2['balancing_period'])
        self.select_radio_balancing_period_units(company2['balancing_period_units'])
        self.fill_field_balancing_period_starts_when(company2['balancing_period_starts_when'])
        self.select_radio_having_benefits(company2['benefits'])
        if len(company2['benefits']) > 0:
            for benefit in company2['benefits']:
                self.click_link_add_benefits()
                self()
                try:
                    self.fill_field_name(benefit['name'])
                    self.fill_field_wage_item_code(benefit['wage_item_code'])
                    self.fill_dropdown_reward_type(benefit['reward_type'])
                    self.fill_field_amount(benefit['reward_type'], benefit['amount'])
                    self.select_radio_for_all_organization_units(benefit['for_all_organization_units'])
                    self.select_radio_for_all_work_positions(benefit['for_all_work_positions'])
                except Exception as e:
                    self.click_link_close()
                    assert False, "Nepovedlo se přidat nový benefit: " + str(e)
                else:
                    self.click_button_save()
                try:
                    self.waiter.wait_for_modal("close")
                except TimeoutException:
                    self()
                    self.click_link_close()
                    assert False, "Nepovedlo se přidat nový benefit!"
        self.click_button_save_and_continue()

    def test_basic_positive(self, company2):
        self.fill_form(company2)
        assert self.screens['company']["3"] in self.driver.current_url, "Nepovedlo se odeslat 2. část formuláře pro vytvoření nové společnosti!"
