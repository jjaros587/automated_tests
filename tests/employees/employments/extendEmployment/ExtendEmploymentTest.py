from tests.BaseTest import BaseTest
from pages.employees.employments.extendEmployment.ExtendEmploymentMasterPage import ExtendEmploymentMasterPage
from ddt import ddt, file_data
from configs.constants import dataPath
from utils.classes.Employee import Employee


@ddt
class ExtendEmploymentTest(BaseTest):
    path = dataPath + 'employees\\employments\\extendEmployment\\'

    @file_data(path + "extend_employment_positive.json")
    def test_add_employment_positive(self, company, employee, inquiry, employment, extend_employment):
        employee_instance = Employee(data={'employee': employee, 'inquiry': inquiry, 'employment': employment})
        self.employees.update({'basic': employee_instance})
        self.ico = company['part1']['identification_code']
        ExtendEmploymentMasterPage(self.driver, employee_instance).fill_form(company, extend_employment)
