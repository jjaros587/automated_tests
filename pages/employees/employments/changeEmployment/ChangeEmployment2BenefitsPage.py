from configs.locators import ChangeEmployment2PageLocators
from utils.utilsTest import select_dropdown_item
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.classes.Waiter import Waiter


class ChangeEmployment2BenefitsPage:

    reward_types = {
        "exact-amount": ChangeEmployment2PageLocators.field_exact_amount,
        "hourly-bonus": ChangeEmployment2PageLocators.field_hourly_amount,
        "percentual-bonus": ChangeEmployment2PageLocators.field_percentual_amount
    }

    locators = {
        "list_containts_benefit": "//*[@id='amendment-benefits-list']//td[@data-before[contains(.,'Typ odměny')]]",
        "link_to_delete": "(//*[@id='amendment-benefits-list']//*[@class='a-remove-benefit'])[1]"
    }

    def __init__(self, driver):
        self.driver = driver
        self.link_add_benefits = self.driver.find_element(*ChangeEmployment2PageLocators.link_add_benefits)
        self.button_save_and_continue = self.driver.find_element(*ChangeEmployment2PageLocators.button_save_and_continue)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.dropdown_type_id = self.driver.find_element(*ChangeEmployment2PageLocators.dropdown_type_id)
        self.button_save = self.driver.find_element(*ChangeEmployment2PageLocators.button_save)
        self.link_close = self.driver.find_element(*ChangeEmployment2PageLocators.link_close)

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

    def fill_form(self, change_employment2):
        try:
            count = len(self.driver.find_elements_by_xpath(self.locators['list_containts_benefit']))
        except NoSuchElementException:
            pass
        else:
            while count > 0:
                count -= 1
                self.driver.find_element_by_xpath(self.locators['link_to_delete']).click()
                self.waiter.wait_for_modal("open", param="remove_benefit")
                self.driver.find_element_by_xpath("//button").click()
                self.waiter.wait_for_modal("close", param="remove_benefit")
        for benefit in change_employment2['benefits']:
            self.add_benefit(benefit)
        self.click_button_save_and_continue()

    def test_basic_positive(self, change_employment2):
        self.fill_form(change_employment2)
        assert 'documents-and-evidence' in self.driver.current_url, "Nepodařilo se odeslat 2. část formuláře pro vytvoření dodatku!"

    def add_benefit(self, benefit):
        self.click_link_add_benefits()
        self()
        try:
            self.fill_dropdown_type_id(benefit['type_id'])
            self.fill_field_amount(benefit['reward_type'], benefit['amount'])
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