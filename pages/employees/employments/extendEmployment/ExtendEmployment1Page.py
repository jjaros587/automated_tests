from utils.utilsTest import select_dropdown_item
from configs.locators import ExtendEmployment1PageLocators


class ExtendEmployment1Page:
    allowed_extensions = {
        "half_year": "Prodloužit o půl roku",
        "one_year": "Prodloužit o rok",
        "two_years": "Prodloužit o 2 roky",
        "three_years": "Prodloužit o 3 roky",
        "specific": "Prodloužit do konkrétního data",
        "indefinite": "Prodloužit na dobu neurčitou",
    }

    def __init__(self, driver):
        self.driver = driver
        self.dropdown_duration_extension_by_months = self.driver.find_element(*ExtendEmployment1PageLocators.dropdown_duration_extension_by_months)
        self.button_save_and_continue = self.driver.find_element(*ExtendEmployment1PageLocators.button_save_and_continue)

    def __call__(self):
        self.field_duration_extension_to_date = self.driver.find_element(*ExtendEmployment1PageLocators.field_duration_extension_to_date)

    def fill_dropdown_duration_extension_by_months(self, duration_extension_by_months):
        if duration_extension_by_months not in self.allowed_extensions:
            raise ValueError("Neplatná hodnota parametru duration_extension_by_months!")
        select_dropdown_item(self.dropdown_duration_extension_by_months, duration_extension_by_months)

    def fill_field_duration_extension_to_date(self, duration_extension_to_date):
        self.field_duration_extension_to_date.clear()
        self.field_duration_extension_to_date.send_keys(duration_extension_to_date)

    def click_button_form_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, extend_employment):
        self.fill_dropdown_duration_extension_by_months(extend_employment['duration_extension_by_months'])
        if extend_employment['duration_extension_by_months'] == self.allowed_extensions['specific']:
            self()
            self.fill_field_duration_extension_to_date(extend_employment['duration_extension_to_date'])
        self.click_button_form_save_and_continue()

    def test_basic_positive(self, extend_employment):
        self.fill_form(extend_employment)
        assert 'documents-and-evidence' in self.driver.current_url, "Nepodařilo se odeslat 1. část formuláře pro prodloužení poměru!"