from tests.BaseTest import BaseTest
from pages.companies.CompaniesPage import CompaniesPage
from pages.navigation.MenuSystemPage import MenuSystemPage
from pages.companies.newCompany.NewCompanyMasterPage import NewCompanyMasterPage
from ddt import ddt, file_data
from configs.constants import dataPath


@ddt
class NewCompanyTest(BaseTest):
    path = dataPath + 'companies\\newCompany\\'

    @file_data(path + "new_company_positive_automatically.json")
    def basic_positive_automatically(self, company):
        self.ico = company['part1']['identification_code']
        NewCompanyMasterPage(self.driver).test_basic_positive(True, company)

    @file_data(path + "new_company_positive.json")
    def test_basic_positive(self, company):
        self.ico = company['part1']['identification_code']
        NewCompanyMasterPage(self.driver).test_basic_positive(False, company)
