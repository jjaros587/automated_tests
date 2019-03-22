from tests.BaseTest import BaseTest
from pages.employees.personalInquiry.PersonalInquiryMasterPage import PersonalInquiryMasterPage
from ddt import ddt, file_data
from configs.constants import dataPath
from utils.classes.Employee import Employee


@ddt
class PersonalInquiryTest(BaseTest):
    path = dataPath + 'employees\\personalInquiry\\'

    @file_data(path + "personal_inquiry_positive.json")
    def test_basic_positive(self, employee, inquiry):
        employee_instance = Employee(data={'employee': employee, 'inquiry': inquiry})
        self.employees.update({'basic': employee_instance})
        PersonalInquiryMasterPage(self.driver, employee_instance).test_basic_positive()

    @file_data(path + "personal_inquiry_negative_empty_fields.json")
    def test_negative_empty_fields_part1(self, employee, inquiry, error):
        employee_instance = Employee(data={'employee': employee, 'inquiry': inquiry})
        self.employees.update({'basic': employee_instance})
        PersonalInquiryMasterPage(self.driver, employee_instance).test_negative_empty_fields_part1(error)


