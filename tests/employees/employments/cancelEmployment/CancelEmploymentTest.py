from pages.employees.employments.cancelEmployment.CancelEmploymentPage import CancelEmploymentPage
from tests.BaseTest import BaseTest
from ddt import ddt, file_data
from configs.constants import dataPath
from utils.classes.Employee import Employee


@ddt
class CancelEmploymentTest(BaseTest):
    path = dataPath + 'employees\\employments\\cancelEmployment\\'

    @file_data(path + "cancel_employment_positive.json")
    def test_cancel_employment_positive(self, company, employee, inquiry, employment, cancel_employment):
        employee_instance = Employee(data={'employee': employee, 'inquiry': inquiry, 'employment': employment})
        self.employees.update({'basic': employee_instance})
        self.ico = company['part1']['identification_code']
        CancelEmploymentPage(self.driver, employee_instance).test_basic_positive(company, cancel_employment)
