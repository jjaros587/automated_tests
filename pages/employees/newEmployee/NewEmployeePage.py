from configs.locators import NewEmployeePageLoators
from utils.utilsTest import select_dropdown_item
from utils.utilsTest import element_exists
from pages.navigation.MenuEmployeesPage import MenuEmployeesPage
from pages.employees.EmployeesPage import EmployeesPage
from utils.utilsTest import get_id_from_url
from selenium.webdriver.common.by import By
import time


class NewEmployeePage:
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance

        '''
        self.dropdown_jazyk = self.driver.find_element(*NewEmployeePageLoators.dropdown_jazyk)
        self.dropdown_útvar = self.driver.find_element(*NewEmployeePageLoators.dropdown_útvar)
        '''

    def __call__(self):
        self.field_name = self.driver.find_element(*NewEmployeePageLoators.field_name)
        self.field_surname = self.driver.find_element(*NewEmployeePageLoators.field_surname)
        self.field_email = self.driver.find_element(*NewEmployeePageLoators.field_email)
        self.field_phone = self.driver.find_element(*NewEmployeePageLoators.field_phone)

        self.dropdown_accessible_for_unit_ids = self.driver.find_element(*NewEmployeePageLoators.dropdown_accessible_for_unit_ids)
        self.dropdown_default_approver_id = self.driver.find_element(*NewEmployeePageLoators.dropdown_default_approver_id)
        self.checkbox_agreement = self.driver.find_element(*NewEmployeePageLoators.checkbox_agreement)
        self.button_save = self.driver.find_element(*NewEmployeePageLoators.button_save)

    def fill_field_name(self, name):
        self.field_name.clear()
        self.field_name.send_keys(name)

    def fill_field_surname(self, surname):
        self.field_surname.clear()
        self.field_surname.send_keys(surname)

    def fill_field_email(self, email):
        self.field_email.clear()
        self.field_email.send_keys(email)

    def fill_field_phone(self, phone):
        self.field_phone.clear()
        self.field_phone.send_keys(phone)

    def fill_dropdown_accessible_for_unit_ids(self, accessible_for_unit_ids):
        select_dropdown_item(self.dropdown_accessible_for_unit_ids, accessible_for_unit_ids)

    def fill_dropdown_default_approver_id(self, default_approver_id):
        time.sleep(0.5)
        select_dropdown_item(self.dropdown_default_approver_id, default_approver_id)

    def click_checkbox_agreement(self):
        self.checkbox_agreement.click()

    def click_button_save(self):
        self.button_save.click()

    def fill_form(self):
        MenuEmployeesPage(self.driver).click_link_employees()
        EmployeesPage(self.driver).click_button_new_employee()
        self()
        employee = self.employee_instance.get_employee()
        self.fill_field_name(employee['name'])
        self.fill_field_surname(employee['surname'])
        self.fill_field_email(self.employee_instance.get_email())
        self.fill_field_phone(employee['phone'])
        self.fill_dropdown_accessible_for_unit_ids(employee['accessible_for_unit_ids'])
        self.fill_dropdown_default_approver_id(employee['default_approver_id'])
        self.click_checkbox_agreement()
        self.click_button_save()

    def test_basic_positive(self):
        self.fill_form()
        assert 'employee-created' in self.driver.current_url, "Zaměstnance se nepovedlo vytvořit!"
        self.employee_instance.set_id(get_id_from_url(self.driver, "employee"))

    def test_basic_negative(self, error):
        self.fill_form()
        if 'employee-created' in self.driver.current_url:
            self.employee_instance.set_id(get_id_from_url(self.driver, "employee"))
            assert False, "Formulář se podařilo odeslat s nevalidními údaji!"
        else:
            assert element_exists(self.driver, (By.ID, error)), "Nebyla zobrazena chybová hláška '%s'!" % error
