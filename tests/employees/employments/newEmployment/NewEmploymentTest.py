from tests.BaseTest import BaseTest
from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from ddt import ddt, file_data
from configs.constants import dataPath
from utils.classes.Employee import Employee


@ddt
class NewEmploymentTest(BaseTest):
    path = dataPath + 'employees\\employments\\newEmployment\\'

    @file_data(path + "new_employment_positive.json")
    def test_add_employment_positive(self, company, employee, inquiry, employment):
        employee_instance = Employee(data={'employee': employee, 'inquiry': inquiry, 'employment': employment})
        self.employees.update({'basic': employee_instance})
        self.ico = company['part1']['identification_code']
        NewEmploymentMasterPage(self.driver, employee_instance).test_basic_positive(company)
