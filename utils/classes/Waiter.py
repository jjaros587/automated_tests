from selenium.common.exceptions import TimeoutException
import time


class Waiter:
    locators = {
        "remove_benefit": "remove-benefit-modal",
        "shift": "shift-form-container",
        "absence": "absence-form-container"
    }
    allowedStates = ["open", "close"]
    allowedParams = ["basic", "remove_benefit", "shift", "absence"]
    fancyBoxLocator = "//*[@class[contains(.,'fancybox-is-open')]]"

    def __init__(self, driver, locator=None, attribute=None, value=None, seconds=6):
        self.driver = driver
        self.seconds = seconds
        self.step = 0.1
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def wait(self, seconds):
        time.sleep(self.step)
        seconds -= self.step

    def wait_for_attribute(self):
        seconds = self.seconds
        while seconds > 0:
            if self.value in self.driver.find_element(*self.locator).get_attribute(self.attribute):
                return
            self.wait(seconds)
        raise TimeoutException

    def wait_attribute_to_be_open(self):
        self.__call__("class", "is-open")
        self.wait_for_attribute()

    def wait_for_modal(self, state, param="basic"):
        if state not in self.allowedStates:
            raise ValueError("Parametr '" + str(state) + "' není platný!")
        if param not in self.allowedParams:
            raise ValueError("Parametr '" + str(param) + "' není platný!")
        if param == "basic":
            self.wait_for_modal_basic(state)
        else:
            self.wait_for_modal_others(state, param)

    # ------------------------------------------------------------------------------------------------------------------
    def wait_for_modal_basic(self, state):
        if state not in self.allowedStates:
            raise ValueError("Parametr '" + str(state) + "' není platný!")
        seconds = self.seconds
        if state == "open":
            while seconds > 0:
                if 'modal' in self.driver.current_url:
                    return
                self.wait(seconds)
        elif state == "close":
            while seconds > 0:
                if 'modal' not in self.driver.current_url:
                    time.sleep(0.5)
                    return
                self.wait(seconds)
        raise TimeoutException

    def wait_for_modal_others(self, state, param):
        seconds = self.seconds
        if state == "open":
            while seconds > 0:
                try:
                    self.driver.find_element_by_id(self.locators[param])
                    self.driver.find_element_by_xpath(self.fancyBoxLocator)
                except Exception as e:
                    self.wait(seconds)
                else:
                    return
        elif state == "close":
            while seconds > 0:
                try:
                    self.driver.find_element_by_id(self.locators[param])
                    self.driver.find_element_by_xpath(self.fancyBoxLocator)
                except Exception as e:
                    time.sleep(0.5)
                    return
                else:
                    self.wait(seconds)
        raise TimeoutException
