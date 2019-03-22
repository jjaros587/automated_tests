from configs.locators import NewCompany4PageLocators
from utils.utilsTest import click_radio_by_value
from selenium.common.exceptions import TimeoutException
import time
from utils.classes.Waiter import Waiter
from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage


class NewCompany4Page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.link_add_organization_unit = self.driver.find_element(*NewCompany4PageLocators.link_add_organization_unit)
        self.button_continue = self.driver.find_element(*NewCompany4PageLocators.button_continue)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.field_name = self.driver.find_element(*NewCompany4PageLocators.field_name)
        self.field_new_cost_center_name = self.driver.find_element(*NewCompany4PageLocators.field_new_cost_center_name)
        self.field_new_cost_center_code = self.driver.find_element(*NewCompany4PageLocators.field_new_cost_center_code)
        self.radio_same_address_as_parent = self.driver.find_elements(*NewCompany4PageLocators.radio_same_address_as_parent)
        self.button_save = self.driver.find_element(*NewCompany4PageLocators.button_save)
        self.link_close = self.driver.find_element(*NewCompany4PageLocators.link_close)

    def click_link_add_organization_unit(self):
        time.sleep(0.5)
        self.link_add_organization_unit.click()
        self.waiter.wait_for_modal("open")

    def fill_field_name(self, name):
        self.field_name.clear()
        self.field_name.send_keys(name)
        self.field_name.send_keys(Keys.TAB)
        time.sleep(0.25)

    def fill_field_new_cost_center_name(self, new_cost_center_name):
        self.field_new_cost_center_name.clear()
        self.field_new_cost_center_name.send_keys(new_cost_center_name)

    def fill_field_new_cost_center_code(self, new_cost_center_code):
        self.field_new_cost_center_code.clear()
        self.field_new_cost_center_code.send_keys(new_cost_center_code)

    def select_radio_same_address_as_parent(self, same_address_as_parent):
        click_radio_by_value(self.radio_same_address_as_parent, same_address_as_parent)

    def click_button_continue(self):
        self.button_continue.click()

    def click_button_save(self):
        self.button_save.click()

    def click_link_close(self):
        self.link_close.click()
        self.waiter.wait_for_modal("close")

    def fill_form(self, company4):
        for item in company4:
            self.click_link_add_organization_unit()
            self()
            try:
                self.fill_field_name(item['name'])
                self.fill_field_new_cost_center_name(item['new_cost_center_name'])
                self.fill_field_new_cost_center_code(item['new_cost_center_code'])
                self.select_radio_same_address_as_parent(item['same_address_as_parent'])
            except Exception as e:
                self.click_link_close()
                assert False, "Nepovedlo se přidat nové středisko: " + str(e)
            else:
                self.click_button_save()
            try:
                self.waiter.wait_for_modal("close")
            except TimeoutException:
                self()
                self.click_link_close()
                assert False, "Nepovedlo se přidat nové středisko!"
        self.click_button_continue()

    def test_basic_positive(self, company4):
        self.fill_form(company4)
        assert self.screens['company']["5"] in self.driver.current_url, "Nepovedlo se odeslat 4. část formuláře pro vytvoření nové společnosti!"
