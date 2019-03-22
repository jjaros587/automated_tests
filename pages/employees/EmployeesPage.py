from configs.locators import EmployeesPageLocators
from utils.utilsTest import select_dropdown_item
from pages.BasePage import BasePage


class EmployeesPage(BasePage):
    allowed_values = {
        "employment": [None, "all", "employees", "active", "terminated", "no-employments", "not-inquiries"],
        "group": [None, "all", "wages-deductions", "not-paying-health-insurance", "foreigners", "soon-expiring-documents", "missing-data"]
    }

    def __init__(self, driver):
        self.driver = driver
        self.button_new_employee = self.driver.find_element(*EmployeesPageLocators.button_new_employee)

    def __call__(self):
        self.__init__(self.driver)

    def click_button_new_employee(self):
        self.button_new_employee.click()
        assert 'new-employee' in self.driver.current_url, "Nedošlo k přesměrování na formulář pro vytvoření nového zaměstnance!"

    def find_employee(self, employment, group, company, employee_id):
        if employment not in self.allowed_values['employment'] or group not in self.allowed_values['group']:
            raise ValueError("Neplatná hodnota parametru!")
        if employment is not None:
            select_dropdown_item(self.driver.find_element(*EmployeesPageLocators.select_employment), employment, "known", deselect=False)
        if group is not None:
            select_dropdown_item(self.driver.find_element(*EmployeesPageLocators.select_group), group, deselect=False)
        if company is not None:
            select_dropdown_item(self.driver.find_element(*EmployeesPageLocators.select_company), company, deselect=False)
        self.driver.find_element(*self.fill_tuple(EmployeesPageLocators.link_employee, employee_id)).click()
        assert "employee-card" in self.driver.current_url
