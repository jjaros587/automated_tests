from configs.locators import AttendanceNewShiftPageLocators
from utils.utilsTest import select_dropdown_item
from utils.classes.Waiter import Waiter
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class AttendanceNewShiftPage:
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance
        self.dropdown_employment = self.driver.find_element(*AttendanceNewShiftPageLocators.dropdown_employment)
        self.field_date_from = self.driver.find_element(*AttendanceNewShiftPageLocators.field_date_from)
        self.field_time_from = self.driver.find_element(*AttendanceNewShiftPageLocators.field_time_from)
        self.field_time_to = self.driver.find_element(*AttendanceNewShiftPageLocators.field_time_to)
        self.dropdown_breaks = self.driver.find_element(*AttendanceNewShiftPageLocators.dropdown_breaks)
        self.dropdown_repetition = self.driver.find_element(*AttendanceNewShiftPageLocators.dropdown_repetition)
        self.dropdown_color = self.driver.find_element(*AttendanceNewShiftPageLocators.dropdown_color)
        self.field_name = self.driver.find_element(*AttendanceNewShiftPageLocators.field_name)
        self.field_note = self.driver.find_element(*AttendanceNewShiftPageLocators.field_note)
        self.button_save = self.driver.find_element(*AttendanceNewShiftPageLocators.button_save)
        self.link_close = self.driver.find_element(*AttendanceNewShiftPageLocators.link_close)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.__init__(self.driver)

    def fill_dropdown_shift_form_employment(self):
        id_employment = self.employee_instance.get_id_employment() + "--" + self.employee_instance.get_id()
        select_dropdown_item(self.dropdown_employment, id_employment, "contains")

    def fill_field_shift_form_date_from(self, date_from):
        self.field_date_from.clear()
        self.field_date_from.send_keys(date_from)
        self.field_date_from.send_keys(Keys.ENTER)

    def fill_field_shift_form_time_from(self, time_from):
        self.field_time_from.clear()
        self.field_time_from.send_keys(time_from)
        self.field_time_from.send_keys(Keys.ENTER)

    def fill_field_shift_form_time_to(self, time_to):
        self.field_time_to.clear()
        self.field_time_to.send_keys(time_to)
        self.field_time_to.send_keys(Keys.ENTER)

    def fill_dropdown_shift_form_breaks(self, breaks):
        select_dropdown_item(self.dropdown_breaks, str(len(breaks)))
        for i, item in enumerate(breaks):
            break_from = self.driver.find_element_by_id("shift_form_break_%s_from" % str(i))
            break_from.clear()
            break_from.send_keys(item['break_from'])
            break_from.send_keys(Keys.ENTER)
            break_to = self.driver.find_element_by_id("shift_form_break_%s_to" % str(i))
            break_to.clear()
            break_to.send_keys(item['break_to'])
            break_to.send_keys(Keys.ENTER)

    def fill_dropdown_shift_form_repetition(self, shift_form_repetition):
        select_dropdown_item(self.dropdown_repetition, shift_form_repetition, "known")

    def fill_dropdown_shift_form_color(self, shift_form_color):
        select_dropdown_item(self.driver, self.dropdown_color, shift_form_color)

    def fill_field_shift_form_name(self, shift_form_name):
        self.field_name.clear()
        self.field_name.send_keys(shift_form_name)

    def fill_field_shift_form_note(self, shift_form_note):
        self.field_note.clear()
        self.field_note.send_keys(shift_form_note)

    def click_button_save(self):
        self.button_save.click()

    def click_link_close(self):
        self.link_close.click()
        self.waiter.wait_for_modal("close", param="shift")

    # --------------------------------------------------------------------------------------------------------
    def fill_form_positive(self, shift):
        try:
            self.fill_dropdown_shift_form_employment()
            self.fill_field_shift_form_date_from(shift['date_from'])
            self.fill_field_shift_form_time_from(shift['time_from'])
            self.fill_field_shift_form_time_to(shift['time_to'])
            self.fill_dropdown_shift_form_breaks(shift['breaks'])
            self.fill_dropdown_shift_form_repetition(shift['repetition'])
        except Exception as e:
            self.click_link_close()
            assert False, "Nepovedlo se přidat novou směnu: " + str(e)
        else:
            self.click_button_save()
        try:
            self.waiter.wait_for_modal("close", param="shift")
        except TimeoutException:
            self()
            self.click_link_close()
            assert False, "Nepovedlo se přidat novou směnu!"