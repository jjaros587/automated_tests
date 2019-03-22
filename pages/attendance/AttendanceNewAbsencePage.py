from configs.locators import AttendanceNewAbsencePageLocators
from utils.utilsTest import select_dropdown_item
from utils.classes.Waiter import Waiter
from selenium.common.exceptions import TimeoutException


class AttendanceNewAbsencePage:
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance

        self.button_save = self.driver.find_element(*AttendanceNewAbsencePageLocators.button_save)
        self.link_close = self.driver.find_element(*AttendanceNewAbsencePageLocators.link_close)
        self.waiter = Waiter(self.driver)

    def __call__(self):
        self.__init__(self.driver)

    def click_button_save(self):
        self.button_save.click()

    def click_link_close(self):
        self.link_close.click()
        self.waiter.wait_for_modal("close")

    # --------------------------------------------------------------------------------------------------------
    def fill_form_positive(self, absence):
        try:
            pass
        except Exception as e:
            self.click_link_close()
            assert False, "Nepovedlo se přidat novou nepřítomnost: " + str(e)
        else:
            self.click_button_save()
        try:
            self.waiter.wait_for_modal("close")
        except TimeoutException:
            self()
            self.click_link_close()
            assert False, "Nepovedlo se přidat novou nepřítomnost!"