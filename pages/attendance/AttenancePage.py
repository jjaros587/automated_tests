from configs.locators import AttendancePageLocators
from pages.attendance.AttendanceNewShiftPage import AttendanceNewShiftPage
from pages.attendance.AttendanceNewAbsencePage import AttendanceNewAbsencePage
from utils.classes.Waiter import Waiter
from utils.utilsTest import select_dropdown_item
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException


class AttendancePage:
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance
        self.dropdown_attendance_company_select = self.driver.find_element(*AttendancePageLocators.dropdown_attendance_company_select)
        self.link_new_absence = self.driver.find_element(*AttendancePageLocators.link_new_absence)
        self.link_new_shift = self.driver.find_element(*AttendancePageLocators.link_new_shift)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.__init__(self.driver, self.employee_instance)

    def fill_dropdown_attendance_company_select(self, company_name):
        select_dropdown_item(self.dropdown_attendance_company_select, company_name, deselect=False)
        time.sleep(0.5)
        self()

    def click_link_new_absence(self):
        self.link_new_absence.click()
        self.waiter.wait_for_modal("open", param="absence")

    def click_link_new_shift(self):
        self.link_new_shift.click()
        self.waiter.wait_for_modal("open", param="shift")

    def test_basic_positive(self):
        attendance = self.employee_instance.get_attendance()
        self.fill_dropdown_attendance_company_select(attendance['company'])
        self.new_shift_positive(attendance['shifts'])
        self.new_absence_positive(attendance['absences'])

    def new_shift_positive(self, shifts):
        for item in shifts:
            self.click_link_new_shift()
            AttendanceNewShiftPage(self.driver, self.employee_instance).fill_form_positive(item)
            self.verify_new_record("shifts", item['date_from'])

    def new_absence_positive(self, absences):
        for item in absences:
            self.click_link_new_absence()
            AttendanceNewAbsencePage(self.driver, self.employee_instance).fill_form_positive(item)
            self.verify_new_record("absences", item['date_from'])

    def verify_new_record(self, param, day_str):
        if param not in ["shifts", "absences"]:
            raise ValueError("Parametr '" + str(param) + "' není platný!")
        while True:
            self()
            day = datetime.strptime(day_str, '%d.%m.%Y')
            current_week = self.driver.find_element_by_id("calendar-date-current").text
            array = current_week.split(" - ")
            day_from = datetime.strptime(array[0] + array[1][3:], '%d.%m.%Y')
            day_to = datetime.strptime(array[1], '%d.%m.%Y')
            if day_from <= day <= day_to:
                day_iso = day.strftime("%Y-%m-%d")
                try:
                    self.driver.find_element_by_xpath("//a[@data-src[contains(.,'%s') and contains(.,'%s') and contains(.,'%s') and contains(.,'%s')]]" % (
                                                          param,
                                                          self.employee_instance.get_id_employment(),
                                                          self.employee_instance.get_id(),
                                                          day_iso
                                                      ))
                except NoSuchElementException:
                    assert False, "V docházkách se nepodařilo vytvořit záznam typu " + param
                else:
                    return
            if day > day_to:
                self.driver.find_element_by_xpath("//a[@class[contains(.,'right')]]").click()
                continue
            if day < day_from:
                self.driver.find_element_by_xpath("//a[@class[contains(.,'left')]]").click()

