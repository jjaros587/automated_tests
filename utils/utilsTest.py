from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import json
from configs.constants import dataPath
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import copy
from configs.constants import select_allowed_cases, checbox_locators, url_delimiters


def scroll_to_top(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)


def get_id_from_url(driver, value):
    if value not in url_delimiters:
        raise ValueError("Parametr '" + str(value) + "' není platný!")
    part = driver.current_url.split(url_delimiters[value])
    link = part[1]
    if value == "employee":
        part = link.split("/")
        return part[0]
    elif value == "user":
        return link


def get_login_credentials():
    with open(dataPath + 'login.json') as file:
        data = json.load(file)
    return data.values()


# --------------------------------------------------------------------------------------------------------------
def element_exists(driver, locator):
    try:
        driver.find_element(*locator)
    except NoSuchElementException:
        return False
    return True


def select_dropdown_item(dropdown, values, case="text", deselect=True):
    if case not in select_allowed_cases:
        raise ValueError("Parametr '" + str(case) + "' není platný!")
    select = Select(dropdown)
    if select.is_multiple:
        select.deselect_all()
    else:
        if deselect:
            select.select_by_value("")
        if values == "":
            return
        values = [values]
    for value in values:
        value = dropdown.find_element(By.XPATH, select_allowed_cases[case] % value).get_attribute("value")
        select.select_by_value(value)


def click_radio_by_value(elements, value):
    for radio in elements:
        if str(value) in radio.get_attribute('value'):
            radio.find_element_by_xpath('..').click()
            return True
    raise NoSuchElementException


def click_checkbox_by_value(elements, values, locator="2"):
    if locator not in checbox_locators:
        raise ValueError("Parametr '" + str(locator) + "' není platný!")
    values_copy = copy.deepcopy(values)
    for checkbox in elements:
        value = checkbox.get_attribute('value')
        if value in values:
            if not checkbox.is_selected():
                checkbox.find_element_by_xpath(checbox_locators[locator]).click()
            values_copy.remove(value)
        elif checkbox.is_selected():
            checkbox.find_element_by_xpath(checbox_locators[locator]).click()
    if len(values_copy) > 0:
        raise NoSuchElementException("V checkboxech nebyly nalenene hodnoty: " + str(values_copy))
