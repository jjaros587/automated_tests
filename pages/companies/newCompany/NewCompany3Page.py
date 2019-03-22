from configs.locators import NewCompany3PageLocators
from pages.BasePage import BasePage


class NewCompany3Page(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.button_continue = self.driver.find_element(*NewCompany3PageLocators.button_continue)

    def __call__(self):
        self.__init__(self.driver)

    def click_button_continue(self):
        self.button_continue.click()

    def fill_form(self, company3):
        self.click_button_continue()

    def test_basic_positive(self, company3):
        self.fill_form(company3)
        assert self.screens['company']["4"] in self.driver.current_url, "Nepovedlo se odeslat 3. část formuláře pro vytvoření nové společnosti!"
