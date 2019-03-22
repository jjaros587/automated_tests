from pages.employees.newEmployee.NewEmployeePage import NewEmployeePage
from pages.employees.personalInquiry.PersonalInquiry1Page import PersonalInquiry1Page
from pages.employees.personalInquiry.PersonalInquiry2Page import PersonalInquiry2Page
from pages.employees.personalInquiry.PersonalInquiry3Page import PersonalInquiry3Page
from configs.locators import OtherLocators
from pages.BasePage import BasePage


class PersonalInquiryMasterPage(BasePage):
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance

    def test_basic_positive(self):
        inquiry = self.start()
        PersonalInquiry1Page(self.driver).test_basic_positive(inquiry['part1'])
        PersonalInquiry2Page(self.driver).test_basic_positive(inquiry['part2'])
        PersonalInquiry3Page(self.driver).test_basic_positive(inquiry['part3'])
        self.driver.find_element(*OtherLocators.button_approve_or_send_to_approval).click()
        assert 'employee-card' in self.driver.current_url, "Nepodařilo se schválit osobní dotazník!"

    def test_negative_empty_fields_part1(self, error):
        inquiry = self.start()
        PersonalInquiry1Page(self.driver).test_negative_empty_fields(inquiry['part1'], error)

    def start(self):
        NewEmployeePage(self.driver, self.employee_instance).test_basic_positive()
        self.driver.find_element_by_link_text("kartu zaměstnance").click()
        self.driver.find_element_by_id("btn-fill-inquiry").click()
        assert self.screens['inquiry']['1'] in self.driver.current_url, "Nedošlo k přesměrování na 1. část formuláře pro osobní dotazník!"
        return self.employee_instance.get_inquiry()



