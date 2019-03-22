from configs.locators import LoginPageLocators
from utils.utilsTest import element_exists
from configs.locators import OtherLocators
from pages.SearchPage import SearchPage
from configs.constants import dataPath
from utils import utilsMain
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self):
        self.field_username = self.driver.find_element(*LoginPageLocators.field_username)
        self.field_password = self.driver.find_element(*LoginPageLocators.field_password)
        self.button_login = self.driver.find_element(*LoginPageLocators.button_login)

    def fill_field_username(self, username):
        self.field_username.clear()
        self.field_username.send_keys(username)

    def fill_field_password(self, password):
        self.field_password.clear()
        self.field_password.send_keys(password)

    def click_button_login(self):
        self.button_login.click()

    def fill_form(self, username, password):
        self()
        self.fill_field_username(username)
        self.fill_field_password(password)
        self.click_button_login()

    def test_basic_positive(self, username, password):
        self.fill_form(username, password)
        assert self.screens['users'] in self.driver.current_url, "Přihlášení se nezdařilo!"

    def test_basic_negative(self, username, password):
        self.fill_form(username, password)
        assert self.screens['users'] not in self.driver.current_url, "Uživatel s nevalidními přístupovými údaji byl přihlášen!"
        assert element_exists(self.driver, LoginPageLocators.alert), "Nezobrazila se chybová hláška!"

    def login_as_user_with_sa_login(self, email):
        LoginPage(self.driver).login_as_super_admin()
        self.login_as_user(email)

    def login_as_user(self, email):
        SearchPage(self.driver).find_user(email)
        self.driver.find_element(*OtherLocators.link_login_as_employee).click()
        assert "employee-card" in self.driver.current_url, "Nepovedlo se přihlásit jako zaměstnanec " + email

    def login_as_super_admin(self):
        self.test_basic_positive(*LoginPage.get_login_credentials())

    @staticmethod
    def get_login_credentials():
        data = utilsMain.get_data_from_json(dataPath + 'login.json')
        return data.values()