from tests.BaseTest import BaseTest
from pages.employees.employments.changeEmployment.ChangeEmploymentMasterPage import ChangeEmploymentMasterPage
from ddt import ddt, file_data
from configs.constants import dataPath
from utils.classes.Employee import Employee


@ddt
class ChangeEmploymentTest(BaseTest):
    path = dataPath + 'employees\\employments\\changeEmployment\\'

    @file_data(path + "change_employment_positive.json")
    def test_change_employment_positive(self, company, employee, inquiry, employment, change_employment):
        employee_instance = Employee(data={'employee': employee, 'inquiry': inquiry, 'employment': employment})
        self.employees.update({'basic': employee_instance})
        self.ico = company['part1']['identification_code']
        ChangeEmploymentMasterPage(self.driver, employee_instance).fill_form(company, change_employment)
