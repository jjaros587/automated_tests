from pages.companies.newCompany.NewCompanyMasterPage import NewCompanyMasterPage
from pages.employees.employments.newEmployment.NewEmploymentMasterPage import NewEmploymentMasterPage
from configs.constants import dataPath
from pages.login.LoginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from utils.classes.ScreenshotListener import ScreenshotListener
from utils.utilsTest import element_exists
from configs.locators import SearchPageLocators
from utils.classes.Employee import Employee
from pages.SearchPage import SearchPage
from tests.BaseTestClassMethods import BaseTestClassMethods
from utils import utilsMain


class PermissionsVisibilityOfEmployeesTest(BaseTestClassMethods):
    path = dataPath + 'companies\\permissions\\'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.create_data()
        cls.driver.quit()

    def setUp(self):
        super().setUp()
        self.driver = super().run_driver()
        self.driver = EventFiringWebDriver(self.driver, ScreenshotListener(self._testMethodName))
        LoginPage(self.driver).login_as_super_admin()

    def tearDown(self):
        self.driver.quit()

    # TESTS -----------------------------------------------------------------------------------------------------------------------
    def test_superior(self):
        email_superior = self.employees['superior'].get_email()
        LoginPage(self.driver).login_as_user(email_superior)
        error = "Nadřízený %s nevidí svého podřízeného %s!"
        self.verify_user(True, email_superior, self.employees['subordinate'].get_inquiry()['part1']['birth_number'], error)
        error = "Nadřízený %s vidí zaměstnance %s, jehož není nadřízeným!"
        self.verify_user(False, email_superior, self.employees['other'].get_inquiry()['part1']['birth_number'], error)
        error = "Nadřízený %s vidí zaměstnance %s, jehož není nadřízeným! Tento zaměstnanec je nadřízeným své pozice!"
        self.verify_user(False,email_superior, self.employees['otherSuperior'].get_inquiry()['part1']['birth_number'], error)

    def test_subordinate(self):
        LoginPage(self.driver).login_as_user(self.employees['subordinate'].get_email())
        if element_exists(self.driver, SearchPageLocators.button_show_search_form):
            self.fail("Zaměstnanci je přístupno vyhledávání i když není ničím nadřízeným!")

    def test_other_superior(self):
        email_other_superior = self.employees['otherSuperior'].get_email()
        LoginPage(self.driver).login_as_user(email_other_superior)
        error = "Zaměstnanec %s vidí jiného zaměstnance %s! Tento zaměstnanec není ničím nadřízeným a je podřízeným jiného zaměstnance!"
        self.verify_user(False, email_other_superior, self.employees['subordinate'].get_inquiry()['part1']['birth_number'], error)
        error = "Zaměstnanec %s vidí jiného zaměstnance %s! Tento zaměstnanec není níčím nadřízeným ani podřízeným!"
        self.verify_user(False, email_other_superior, self.employees['other'].get_inquiry()['part1']['birth_number'], error)
        error = "Zaměstnanec %s vidí jiného zaměstnance %s! Tento Zaměstnanec je něčím nadřízeným!"
        self.verify_user(False, email_other_superior, self.employees['superior'].get_inquiry()['part1']['birth_number'], error)

    def test_other(self):
        LoginPage(self.driver).login_as_user(self.employees['other'].get_email())
        if element_exists(self.driver, SearchPageLocators.button_show_search_form):
            self.fail("Zaměstnanci je přístupno vyhledávání i když není ničím nadřízeným!")

    # OTHER METHODS ---------------------------------------------------------------------------------------------------------------------
    @classmethod
    def create_data(cls):
        try:
            data = utilsMain.get_data_from_json(cls.path + 'permissions_visibility_of_employees.json')
            cls.ico = data['company']['part1']['identification_code']
            cls.employees.update({
                'superior':         Employee(data=data['superior']),
                'subordinate':      Employee(data=data['subordinate']),
                'other':            Employee(data=data['other']),
                'otherSuperior':    Employee(data=data['otherSuperior'])
            })
            NewCompanyMasterPage(cls.driver).test_basic_positive(False, data['company'])
            NewEmploymentMasterPage(cls.driver, cls.employees['superior']).add_employment_without_company()
            NewEmploymentMasterPage(cls.driver, cls.employees['subordinate']).add_employment_without_company()
            NewEmploymentMasterPage(cls.driver, cls.employees['other']).add_employment_without_company()
            NewEmploymentMasterPage(cls.driver, cls.employees['otherSuperior']).add_employment_without_company()
        except Exception as e:
            cls.createFail = "SELHALO VYTVOŘENÍ DAT:\n\n" + str(e)

    def verify_user(self, should_see, email, test_rc, error):
        SearchPage(self.driver).find_user_basic(test_rc)
        if should_see:
            assert "employee-card" in self.driver.current_url, error % (email, test_rc)
        else:
            assert "employee-card" not in self.driver.current_url, error % (email, test_rc)


