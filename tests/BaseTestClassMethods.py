from pages.login.LoginPage import LoginPage
from tests.SuperTest import SuperTest


class BaseTestClassMethods(SuperTest):
    createFail = None

    @classmethod
    def setUpClass(cls):
        cls.driver = super().run_driver()
        LoginPage(cls.driver).login_as_super_admin()

    def setUp(self):
        if self.createFail is not None:
            self.fail(self.createFail)

    @classmethod
    def tearDownClass(cls):
        cls.driver = super().run_driver()
        LoginPage(cls.driver).login_as_super_admin()
        super().delete_users(cls.driver, cls.employees)
        super().delete_company(cls.driver, cls.ico)
        cls.driver.quit()
