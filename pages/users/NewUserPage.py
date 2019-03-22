from configs.locators import NewUserPageLocators
from utils.utilsTest import click_checkbox_by_value
from utils.utilsTest import element_exists
from utils.utilsTest import get_id_from_url
from selenium.webdriver.common.by import By


class NewUserPage:
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance

    def __call__(self):
        self.field_name = self.driver.find_element(*NewUserPageLocators.field_name)
        self.field_surname = self.driver.find_element(*NewUserPageLocators.field_surname)
        self.field_email = self.driver.find_element(*NewUserPageLocators.field_email)
        self.field_phone = self.driver.find_element(*NewUserPageLocators.field_phone)
        self.checkbox_user_roles = self.driver.find_elements(*NewUserPageLocators.checkbox_user_roles)
        self.checkbox_agreement = self.driver.find_element(*NewUserPageLocators.checkbox_agreement)
        self.button_save = self.driver.find_element(*NewUserPageLocators.button_save)

    def fill_field_jmeno(self, name):
        self.field_name.clear()
        self.field_name.send_keys(name)

    def fill_field_prijmeni(self, surname):
        self.field_surname.clear()
        self.field_surname.send_keys(surname)

    def fill_field_email(self, email):
        self.field_email.clear()
        self.field_email.send_keys(email)

    def fill_field_telefon(self, phone):
        self.field_phone.clear()
        self.field_phone.send_keys(phone)

    def click_checkbox_role(self, role):
        click_checkbox_by_value(self.checkbox_user_roles, role)

    def click_checkbox_souhlas(self):
        self.checkbox_agreement.click()

    def click_button_zalozit(self):
        self.button_save.click()

    def fill_form(self, email, data):
        self.driver.find_element_by_link_text("Přidat uživatele").click()
        self.__call__()
        self.fill_field_jmeno(data['name'])
        self.fill_field_prijmeni(data['surname'])
        self.fill_field_email(email)
        self.fill_field_telefon(data['phone'])
        self.click_checkbox_role(data['role'])
        self.click_checkbox_souhlas()
        self.click_button_zalozit()

    def test_basic_positive(self):
        self.fill_form(self.employee_instance.get_email(), self.employee_instance.get_user())
        assert 'user-created' in self.driver.current_url, "Nepovedlo se vytvořit systémového uživatele!"
        self.employee_instance.set_id(get_id_from_url(self.driver, "user"))

    def test_negative_empty_fields(self, error):
        self.fill_form(self.employee_instance.get_email(), self.employee_instance.get_user())
        if 'user-created' in self.driver.current_url:
            self.employee_instance.set_id(get_id_from_url(self.driver, "user"))
            assert False, "Formulář pro vytvoření uživatele se povedlo odeslat s nevalidními hodnotami!"
        else:
            assert element_exists(self.driver, (By.ID, error)), "Nebyla zobrazena chybová hláška '%s'!" % error