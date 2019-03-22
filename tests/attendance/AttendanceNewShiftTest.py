from tests.BaseTestClassMethods import BaseTestClassMethods
from utils.classes.Employee import Employee
from configs.constants import dataPath
from utils import utilsMain
from pages.companies.newCompany.NewCompanyMasterPage import NewCompanyMasterPage
from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from pages.login.LoginPage import LoginPage
from pages.navigation.MenuAttendancePage import MenuAttendancePage
from pages.attendance.AttenancePage import AttendancePage


class AttendanceNewShiftTest(BaseTestClassMethods):
    path = dataPath + 'attendance\\'
    company = None
    employment_page = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.create_data()
        cls.driver.quit()

    def setUp(self):
        super().setUp()
        self.driver = super().run_driver()
        LoginPage(self.driver).login_as_super_admin()
        MenuAttendancePage(self.driver).click_link_plan()

    def tearDown(self):
        self.driver.quit()

    # TESTS -----------------------------------------------------------------------------------------------------------------------
    def test_add_new_shift(self):
        AttendancePage(self.driver, self.employees['basic']).test_basic_positive()

    def add_new_absence(self):
        AttendancePage(self.driver, self.employees['basic']).test_basic_positive()

    # OTHER METHODS ---------------------------------------------------------------------------------------------------------------
    @classmethod
    def create_data(cls):
        try:
            data = utilsMain.get_data_from_json(cls.path + 'attendance_shifts.json')
            cls.ico = data['company']['part1']['identification_code']
            cls.company = data['company']['part1']['name']
            cls.employees.update({
                'basic': Employee(data=data['employee1']),
            })
            NewCompanyMasterPage(cls.driver).test_basic_positive(False, data['company'])
            NewEmploymentMasterPage(cls.driver, cls.employees['basic']).add_employment_without_company()
        except Exception as e:
            cls.createFail = "SELHALO VYTVOŘENÍ DAT:\n\n" + str(e)