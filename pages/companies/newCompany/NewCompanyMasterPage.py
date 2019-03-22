from pages.companies.CompaniesPage import CompaniesPage
from pages.navigation.MenuSystemPage import MenuSystemPage
from pages.companies.newCompany.NewCompany1Page import NewCompany1Page
from pages.companies.newCompany.NewCompany2Page import NewCompany2Page
from pages.companies.newCompany.NewCompany3Page import NewCompany3Page
from pages.companies.newCompany.NewCompany4Page import NewCompany4Page
from pages.companies.newCompany.NewCompany5Page import NewCompany5Page
from pages.BasePage import BasePage


class NewCompanyMasterPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self):
        self.__init__(self.driver)

    def fill_form(self):
        pass

    def test_basic_positive(self, automatically, company):
        MenuSystemPage(self.driver).click_link_companies()
        CompaniesPage(self.driver).add_company(company['country'])
        assert self.screens['company']["1"] % company['country'] in self.driver.current_url, "Nedošlo k přesměrování na formulář pro vytvoření nové společnosti!"

        NewCompany1Page(self.driver).test_basic_positive(automatically, company['part1'])
        NewCompany2Page(self.driver).test_basic_positive(company['part2'])
        NewCompany3Page(self.driver).test_basic_positive(company['part3'])
        NewCompany4Page(self.driver).test_basic_positive(company['part4'])
        NewCompany5Page(self.driver).test_basic_positive(company['part5'])