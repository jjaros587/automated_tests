from pages.employees.employments.extendEmployment.ExtendEmployment1Page import ExtendEmployment1Page
from pages.employees.employments.extendEmployment.ExtendEmployment2Page import ExtendEmployment2Page
from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from pages.employees.employments.BaseChangePage import BaseChangePage
from configs.locators import BaseChangePageLocators


class ExtendEmploymentMasterPage(BaseChangePage):
    def __init__(self, driver, employee_isntance):
        super().__init__(driver, employee_isntance)

    def fill_form(self, company, extend_employment):
        NewEmploymentMasterPage(self.driver, self.employee_instance).test_basic_positive(company)

        self.go_extend()
        ExtendEmployment1Page(self.driver).test_basic_positive(extend_employment)
        ExtendEmployment2Page(self.driver).test_basic_positive()

        self.driver.find_element(*BaseChangePageLocators.button_create_amendment).click()
        assert 'created' in self.driver.current_url, "Nepodařilo se schválit prodloužení poměru!"