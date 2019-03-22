from configs.locators import ChangeEmployment3PageLocators


class ChangeEmployment3Page:
    def __init__(self, driver):
        self.driver = driver
        self.button_save_and_finish = self.driver.find_element(*ChangeEmployment3PageLocators.button_save_and_finish)

    def __call__(self):
        self.__init__(self.driver)

    def click_button_save_and_finish(self):
        self.button_save_and_finish.click()

    def fill_form(self, change_employment3):
        self.click_button_save_and_finish()

    def test_basic_positive(self, change_employment3):
        self.fill_form(change_employment3)
        assert 'summary' in self.driver.current_url, "Nepodařilo se odeslat 3. část formuláře pro vytvoření dodatku!"