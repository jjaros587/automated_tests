from tests.BaseTest import BaseTest
from pages.navigation.MenuEmployeesPage import MenuEmployeesPage
from pages.navigation.MenuAttendancePage import MenuAttendancePage
from pages.navigation.MenuRequestsPage import MenuRequestsPage
from pages.navigation.MenuSystemPage import MenuSystemPage
from ddt import ddt


@ddt
class MainMenuTest(BaseTest):

    def test_menu(self):
        self.employees_menu()
        self.attendance_menu()
        self.requests_menu()
        self.system_menu()

    def employees_menu(self):
        employees = MenuEmployeesPage(self.driver)
        employees.click_link_employees()
        employees().click_link_document_definitions()
        employees().click_link_changes()
        employees().click_link_changes_new()
        employees().click_link_documents_overview()

    def attendance_menu(self):
        attendance = MenuAttendancePage(self.driver)
        attendance.click_link_plan()
        attendance().click_link_closing()

    def requests_menu(self):
        MenuRequestsPage(self.driver).click_approval_requests()

    def system_menu(self):
        system = MenuSystemPage(self.driver)
        system.click_link_users()
        system().click_link_roles()
        system().click_link_companies()
        system().click_link_system_settings()
        system().click_link_licence()

