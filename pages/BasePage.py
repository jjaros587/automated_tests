from configs import constants
import requests
from configs.constants import screens


class BasePage:
    screens = screens

    @staticmethod
    def verify_page_status_code(driver):
        r = requests.get(driver.current_url)
        status = str(r.status_code)
        if status[0] in constants.unwanted_status_codes:
            assert False, "Stránka vyhodila HTTP error " + status

    @staticmethod
    def fill_tuple(locator, value):
        (a, b) = locator
        return a, b % value
