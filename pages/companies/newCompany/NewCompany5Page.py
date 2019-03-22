from configs.locators import NewCompany5PageLocators
from utils.utilsTest import click_radio_by_value
from utils.utilsTest import select_dropdown_item
from utils.utilsTest import click_checkbox_by_value
from selenium.common.exceptions import TimeoutException
import time
from utils.classes.Waiter import Waiter
from pages.BasePage import BasePage


class NewCompany5Page(BasePage):
    roles = {
        "superior": "ROLE_SUPERIOR",
        "approver": "ROLE_APPROVER",
        "attendance_manager": "ROLE_ATTENDANCE_MANAGER"
    }

    def __init__(self, driver):
        self.driver = driver
        self.link_add_work_position = self.driver.find_element(*NewCompany5PageLocators.link_add_work_position)
        self.button_finish = self.driver.find_element(*NewCompany5PageLocators.button_finish)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.field_name = self.driver.find_element(*NewCompany5PageLocators.field_name)
        self.field_localized_names_for_contract_cs = self.driver.find_element(*NewCompany5PageLocators.field_localized_names_for_contract_cs)
        self.radio_for_all_organization_units = self.driver.find_elements(*NewCompany5PageLocators.radio_for_all_organization_units)
        self.radio_managing_position = self.driver.find_elements(*NewCompany5PageLocators.radio_managing_position)
        self.dropdown_medical_examination_work_category = self.driver.find_element(*NewCompany5PageLocators.dropdown_medical_examination_work_category)
        self.dropdown_job_group = self.driver.find_element(*NewCompany5PageLocators.dropdown_job_group)
        self.dropdown_shift_type = self.driver.find_element(*NewCompany5PageLocators.dropdown_shift_type)
        self.radio_working_hours_type = self.driver.find_elements(*NewCompany5PageLocators.radio_working_hours_type)
        self.dropdown_default_trial_period_months = self.driver.find_element(*NewCompany5PageLocators.dropdown_default_trial_period_months)
        self.dropdown_job_classification_id = self.driver.find_element(*NewCompany5PageLocators.dropdown_job_classification_id)
        self.checkbox_roles = self.driver.find_elements(*NewCompany5PageLocators.checkbox_roles)

        self.button_save = self.driver.find_element(*NewCompany5PageLocators.button_save)
        self.link_close = self.driver.find_element(*NewCompany5PageLocators.link_close)

    def click_link_add_work_position(self):
        time.sleep(0.5)
        self.link_add_work_position.click()
        self.waiter.wait_for_modal("open")

    def fill_field_name(self, name):
        self.field_name.clear()
        self.field_name.send_keys(name)

    def fill_field_localized_names_for_contract_cs(self, localized_names_for_contract_cs):
        self.field_localized_names_for_contract_cs.click()
        self.field_localized_names_for_contract_cs.clear()
        self.field_localized_names_for_contract_cs.send_keys(localized_names_for_contract_cs)

    def select_radio_for_all_organization_units(self, organization_units_ids):
        value = "1" if len(organization_units_ids) == 0 else "0"
        click_radio_by_value(self.radio_for_all_organization_units, value)

    def fill_dropdown_organization_units_ids(self, organization_units_ids):
        if len(organization_units_ids) > 0:
            element = self.driver.find_element(*NewCompany5PageLocators.dropdown_organization_units_ids)
            select_dropdown_item(element, organization_units_ids)

    def select_radio_managing_position(self, managing_position):
        click_radio_by_value(self.radio_managing_position, managing_position)

    def fill_dropdown_medical_examination_work_category(self, medical_examination_work_category):
        select_dropdown_item(self.dropdown_medical_examination_work_category, medical_examination_work_category)

    def fill_dropdown_job_group(self, job_group):
        select_dropdown_item(self.dropdown_job_group, job_group)

    def fill_dropdown_shift_type(self, shift_type):
        select_dropdown_item(self.dropdown_shift_type, shift_type)

    def select_radioworking_hours_type(self, working_hours_type):
        click_radio_by_value(self.radio_working_hours_type, working_hours_type)

    def fill_dropdown_default_trial_period_months(self, default_trial_period_months):
        select_dropdown_item(self.dropdown_default_trial_period_months, default_trial_period_months)

    def fill_dropdown_job_classification_id(self, job_classification_id):
        select_dropdown_item(self.dropdown_job_classification_id, job_classification_id, "known")

    def click_checkbox_role(self, roles):
        for role in roles:
            if role not in self.roles.values():
                raise ValueError("Nesprávná hodnota parametru roles")
        click_checkbox_by_value(self.checkbox_roles, roles)

    def fill_dropdown_superior_of_position_ids(self, superior_of_position_ids):
        element = self.driver.find_element(*NewCompany5PageLocators.dropdown_superior_of_position_ids)
        select_dropdown_item(element, superior_of_position_ids)

    def click_button_finish(self):
        self.button_finish.click()

    def click_button_save(self):
        self.button_save.click()

    def click_link_close(self):
        self.link_close.click()
        self.waiter.wait_for_modal("close")

    def fill_form(self, company5):
        for item in company5:
            self.click_link_add_work_position()
            self()
            try:
                self.fill_field_name(item['name'])
                self.fill_field_localized_names_for_contract_cs(item['localized_names_for_contract_cs'])
                self.select_radio_for_all_organization_units(item['organization_units_ids'])
                self.fill_dropdown_organization_units_ids(item['organization_units_ids'])
                self.select_radio_managing_position(item['managing_position'])
                self.fill_dropdown_medical_examination_work_category(item['medical_examination_work_category'])
                self.fill_dropdown_job_group(item['job_group'])
                self.fill_dropdown_shift_type(item['shift_type'])
                self.select_radioworking_hours_type(item['working_hours_type'])
                self.fill_dropdown_default_trial_period_months(item['default_trial_period_months'])
                self.fill_dropdown_job_classification_id(item['job_classification_id'])
                self.click_checkbox_role(item['roles'])
                if "ROLE_SUPERIOR" in item['roles']:
                    self.fill_dropdown_superior_of_position_ids(item['superior_of_position_ids'])
            except Exception as e:
                self.click_link_close()
                assert False, "Nepovedlo se přidat novou pozici: " + str(e)
            else:
                self.click_button_save()
            try:
                self.waiter.wait_for_modal("close")
            except TimeoutException:
                self()
                self.click_link_close()
                assert False, "Nepovedlo se přidat novou pozici!"
        self.click_button_finish()

    def test_basic_positive(self, company5):
        self.fill_form(company5)
        assert self.screens['company']["finish"] in self.driver.current_url, "Nepovedlo se odeslat 5. část formuláře pro vytvoření nové společnosti!"
