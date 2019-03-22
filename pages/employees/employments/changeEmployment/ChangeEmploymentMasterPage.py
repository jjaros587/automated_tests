from pages.employees.employments.changeEmployment.ChangeEmployment1Page import ChangeEmployment1Page
from pages.employees.employments.changeEmployment.ChangeEmployment2BenefitsPage import ChangeEmployment2BenefitsPage
from pages.employees.employments.changeEmployment.ChangeEmployment2OthersPage import ChangeEmployment2OthersPage
from pages.employees.employments.changeEmployment.ChangeEmployment3Page import ChangeEmployment3Page
from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from pages.employees.employments.BaseChangePage import BaseChangePage
from configs.locators import BaseChangePageLocators


class ChangeEmploymentMasterPage(BaseChangePage):
    def __init__(self, driver, employee_isntance):
        super().__init__(driver, employee_isntance)

    def fill_form(self, company, change_employment):
        NewEmploymentMasterPage(self.driver, self.employee_instance).test_basic_positive(company)

        self.go_change()
        changes = list(change_employment['part2'].keys())
        ChangeEmployment1Page(self.driver).test_basic_positive(change_employment['part1'], changes)

        count = len(changes)
        if count > 1 or (count == 1 and "benefits" not in changes):
            ChangeEmployment2OthersPage(self.driver, changes).test_basic_positive(change_employment['part2'])
        if "benefits" in changes:
            ChangeEmployment2BenefitsPage(self.driver).test_basic_positive(change_employment['part2'])

        ChangeEmployment3Page(self.driver).test_basic_positive(change_employment['part3'])

        self.driver.find_element(*BaseChangePageLocators.button_create_amendment).click()
        assert 'created' in self.driver.current_url, "Nepodařilo se schválit dodatek pracovního poměru!"



