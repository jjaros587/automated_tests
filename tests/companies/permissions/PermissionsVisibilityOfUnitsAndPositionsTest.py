from pages.companies.newCompany.NewCompanyMasterPage import NewCompanyMasterPage
from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from pages.employees.personalInquiry.PersonalInquiryMasterPage import PersonalInquiryMasterPage
from pages.employees.EmployeeCardPage import EmployeeCardPage
from configs.constants import dataPath
from utils import utilsMain
from pages.login.LoginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from utils.classes.ScreenshotListener import ScreenshotListener
from tests.BaseTestClassMethods import BaseTestClassMethods
from utils.classes.Employee import Employee
from pages.navigation.MenuEmployeesPage import MenuEmployeesPage
from pages.employees.EmployeesPage import EmployeesPage
from pages.employees.employments.newEmployment.NewEmployment1Page import NewEmployment1Page
from selenium.common.exceptions import NoSuchElementException


class PermissionsVisibilityOfUnitsAndPositionsTest(BaseTestClassMethods):
    path = dataPath + 'companies\\permissions\\'
    company = None
    employment_page = None
    test_data = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.create_data()
        if cls.createFail is None:
            try:
                LoginPage(cls.driver).login_as_user(cls.employees['superior'].get_email())
                MenuEmployeesPage(cls.driver).click_link_employees()
                EmployeesPage(cls.driver).find_employee("no-employments", None, cls.company, cls.employees['subordinate'].get_id())
                EmployeeCardPage(cls.driver).add_employment(cls.company)
                cls.employment_page = NewEmployment1Page(cls.driver)
                cls.employment_page.select_radio_type(cls.test_data['type'])
                cls.employment_page.fill_field_start_date(cls.test_data['start_date'])
                cls.employment_page.fill_filed_boarding_date(cls.test_data['boarding_date'])
            except Exception as e:
                cls.createFail = str(e)
                cls.driver.quit()
        else:
            cls.driver.quit()

    def setUp(self):
        super().setUp()
        self.driver = EventFiringWebDriver(self.driver, ScreenshotListener(self._testMethodName))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    # TESTS -----------------------------------------------------------------------------------------------------------------------
    def test_superior_see_units_should_see(self):
        try:
            self.employment_page.fill_dropdown_organization_unit_id(self.test_data['test_superior_see_units_should_see'])
        except NoSuchElementException:
            self.fail("Vedoucí nevidí útvar, jehož je nadřízeným!")
        else:
            return

    def test_superior_do_not_see_unit_should_not_see(self):
        try:
            self.employment_page.fill_dropdown_organization_unit_id(self.test_data['test_superior_do_not_see_unit_should_not_see'])
        except NoSuchElementException:
            return
        else:
            self.fail("Vedoucí vidí útvar, jehož není nadřízeným!")

    def test_superior_see_position_in_his_unit_should_see(self):
        self.employment_page.fill_dropdown_organization_unit_id(self.test_data['test_superior_see_units_should_see'])
        try:
            self.employment_page.fill_dropdown_work_position_id(
                self.test_data['superior_see_position_in_his_unit_should_see'])
        except NoSuchElementException:
            self.fail("Vedoucí nevidí pozici, jejíž je nadřízený!")
        else:
            return

    def test_superior_do_not_see_position_in_his_unit_should_not_see(self):
        self.employment_page.fill_dropdown_organization_unit_id(self.test_data['test_superior_see_units_should_see'])
        try:
            self.employment_page.fill_dropdown_work_position_id(self.test_data['superior_do_not_see_position_in_his_unit_should_not_see'])
        except NoSuchElementException:
            return
        else:
            self.fail("Vedoucí vidí v útvaru, jehož je nadřízený pozici, jejíž není nadřízený!")

    def test_superior_do_not_see_position_in_another_unit_should_not_see(self):
        self.employment_page.fill_dropdown_organization_unit_id(self.test_data['test_superior_see_units_should_see'])
        try:
            self.employment_page.fill_dropdown_work_position_id(self.test_data['superior_do_not_see_position_in_another_unit_should_not_see'])
        except NoSuchElementException:
            return
        else:
            self.fail("Vedoucí vidí pozici, jejíž není nadřízený v útvaru, jehož není nadřízený!")

    def test_superior_do_not_see_position_in_another_unit_which_is_superior_should_not_see(self):
        self.employment_page.fill_dropdown_organization_unit_id(self.test_data['test_superior_see_units_should_see'])
        try:
            self.employment_page.fill_dropdown_work_position_id(self.test_data['superior_do_not_see_position_in_another_unit_which_is_superior_should_not_see'])
        except NoSuchElementException:
            return
        else:
            self.fail("Vedoucí vidí pozici, jejíž je nadřízený v útvaru, jehož není nadřízený!")

    # OTHER METHODS ---------------------------------------------------------------------------------------------------------------
    @classmethod
    def create_data(cls):
        try:
            data = utilsMain.get_data_from_json(cls.path + 'permissions_visibility_of_units_and_positions.json')
            cls.test_data = data['test_data']
            cls.ico = data['company']['part1']['identification_code']
            cls.company = data['company']['part1']['name']
            cls.employees.update({
                'superior': Employee(data=data['superior']),
                'subordinate': Employee(data=data['subordinate'])
            })
            NewCompanyMasterPage(cls.driver).test_basic_positive(False, data['company'])
            NewEmploymentMasterPage(cls.driver, cls.employees['superior']).add_employment_without_company()
            PersonalInquiryMasterPage(cls.driver, cls.employees['subordinate']).test_basic_positive()
        except Exception as e:
            cls.createFail = "SELHALO VYTVOŘENÍ DAT:\n\n" + str(e)
