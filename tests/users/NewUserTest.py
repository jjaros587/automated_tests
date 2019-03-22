from tests.BaseTest import BaseTest
from pages.users.NewUserPage import NewUserPage
from configs.constants import dataPath
from ddt import ddt, file_data
from utils.classes.Employee import Employee


@ddt
class NewUserTest(BaseTest):
    path = dataPath + "users/"

    @file_data(path + "new_user_positive.json")
    def test_positive(self, user):
        employee_instance = Employee(data={'user': user})
        self.employees.update({'basic': employee_instance})
        NewUserPage(self.driver, employee_instance).test_basic_positive()

    @file_data(path + "new_user_negative_empty_fields.json")
    def test_negative_empty_fields(self, user, error):
        employee_instance = Employee(data={'user': user})
        self.employees.update({'basic': employee_instance})
        NewUserPage(self.driver, employee_instance).test_negative_empty_fields(error)
