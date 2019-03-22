from configs.locators import NewEmployment4PageLocators


class NewEmployment4Page:
    def __init__(self, driver):
        self.driver = driver
        self.button_save_and_continue = self.driver.find_element(*NewEmployment4PageLocators.button_save_and_continue)

    def __call__(self):
        self.__init__(self.driver)

    def click_button_save_and_continue(self):
        self.button_save_and_continue.click()

    def fill_form(self, employment4):
        self.click_button_save_and_continue()

    def test_basic_positive(self, employment4):
        self.fill_form(employment4)
        assert 'summary' in self.driver.current_url, "Nepovedlo se odeslat 2. část formuláře pro vytvoření poměru!"

