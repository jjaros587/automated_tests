from tests.BaseTest import BaseTest
from pages.employees.newEmployee.NewEmployeePage import NewEmployeePage
from ddt import ddt, file_data
from configs.constants import dataPath
from utils.classes.Employee import Employee


@ddt
class NewEmployeeTest(BaseTest):
    path = dataPath + 'employees\\newEmployee\\'

    @file_data(path + "new_employee_positive.json")
    def test_add_employee_positive(self, employee):
        employee_instance = Employee(data={'employee': employee})
        self.employees.update({'basic': employee_instance})
        NewEmployeePage(self.driver, employee_instance).test_basic_positive()

    @file_data(path + "new_employee_negative.json")
    def test_add_employee_mandatory_field_empty(self, employee, error):
        employee_instance = Employee(data={'employee': employee})
        self.employees.update({'basic': employee_instance})
        NewEmployeePage(self.driver, employee_instance).test_basic_negative(error)
