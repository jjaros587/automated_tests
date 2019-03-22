import unittest
from pages.navigation.MenuSystemPage import MenuSystemPage
from pages.companies.CompaniesPage import CompaniesPage
from utils.utilsTest import scroll_to_top
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from configs.config import delete_fails_log
import os
import logging
from configs.constants import environments
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class SuperTest(unittest.TestCase):
    driver = None
    ico = None
    employees = {}

    @staticmethod
    def delete_company(driver, ico):
        if ico is not None:
            scroll_to_top(driver)
            MenuSystemPage(driver).click_link_companies()
            if not CompaniesPage(driver).delete_company(ico):
                SuperTest.insert_delete_fail("Společnost s ičo '" + ico + "' se nepovedlo smazat!")

    @staticmethod
    def delete_users(driver, employees):
        if not employees:
            return
        for key, employee in employees.items():
            if employee.get_id() is not None:
                url = environments[os.environ.get('env')] + "users/delete-user/" + employee.get_id()
                driver.get(url)
                if ("status" and "OK") not in driver.page_source:
                    SuperTest.insert_delete_fail("Uživatele s emailem '" + employee.get_email() + "' se nepovedlo smazat!")
                driver.back()

    @staticmethod
    def run_driver():
        driver = None
        if os.environ.get('BROWSER') == "chrome":
            chrome_options = webdriver.chrome.options.Options()
            if os.environ.get('headless') == "True":
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())
        elif os.environ.get('BROWSER') == "firefox":
            firefox_options = webdriver.firefox.options.Options()
            if os.environ.get('headless') == "True":
                firefox_options.headless = True
            driver = webdriver.Firefox(options=firefox_options, executable_path=GeckoDriverManager().install())
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(environments[os.environ.get('env')])
        return driver

    @staticmethod
    def insert_delete_fail(message):
        file = delete_fails_log
        os.makedirs(os.path.dirname(file), exist_ok=True)
        logging.basicConfig(filename=file,
                            filemode='a',
                            format='%(message)s')
        logging.error(message)
