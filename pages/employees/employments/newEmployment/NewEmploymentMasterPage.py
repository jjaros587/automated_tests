from pages.employees.employments.newEmployment.NewEmployment1Page import NewEmployment1Page
from pages.employees.employments.newEmployment.NewEmployment2Page import NewEmployment2Page
from pages.employees.employments.newEmployment.NewEmployment3Page import NewEmployment3Page
from pages.employees.employments.newEmployment.NewEmployment4Page import NewEmployment4Page
from pages.employees.EmployeeCardPage import EmployeeCardPage
from pages.employees.personalInquiry.PersonalInquiryMasterPage import PersonalInquiryMasterPage
from pages.companies.newCompany.NewCompanyMasterPage import NewCompanyMasterPage
from configs.locators import OtherLocators
from pages.BasePage import BasePage


class NewEmploymentMasterPage(BasePage):
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance

    def test_basic_positive(self, company):
        NewCompanyMasterPage(self.driver).test_basic_positive(False, company)
        self.add_employment_without_company()

    def add_employment_without_company(self):
        PersonalInquiryMasterPage(self.driver, self.employee_instance).test_basic_positive()
        employment = self.employee_instance.get_employment()
        EmployeeCardPage(self.driver).add_employment(employment['company'])
        assert self.screens['newEmployment']['1'] in self.driver.current_url, "Nepovedlo se přejít na 1. část formuláře pro vytvoření poměru!"
        NewEmployment1Page(self.driver).test_basic_positive(employment['part1'], self.employee_instance)
        NewEmployment2Page(self.driver).test_basic_positive(employment['part2'])
        NewEmployment3Page(self.driver).test_basic_positive(employment['part3'])
        NewEmployment4Page(self.driver).test_basic_positive(employment['part4'])
        self.driver.find_element(*OtherLocators.button_create_employment).click()
        assert 'created' in self.driver.current_url, "Nepovedlo se schválit nový poměr!"



