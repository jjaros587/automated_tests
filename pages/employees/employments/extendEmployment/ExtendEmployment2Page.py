from configs.locators import ExtendEmployment2PageLocators


class ExtendEmployment2Page:
    def __init__(self, driver):
        self.driver = driver
        self.button_save_and_finish = self.driver.find_element(*ExtendEmployment2PageLocators.button_save_and_finish)

    def click_button_save_and_finish(self):
        self.button_save_and_finish.click()

    def test_basic_positive(self):
        self.click_button_save_and_finish()
        assert 'summary' in self.driver.current_url, "Nepodařilo se odeslat 2. část formuláře pro prodloužení poměru!"