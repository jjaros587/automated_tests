from configs.locators import BaseChangePageLocators, OtherLocators


class BaseChangePage:
    def __init__(self, driver, employee_instance):
        self.driver = driver
        self.employee_instance = employee_instance

    def go(self):
        self.driver.find_element(*OtherLocators.link_employee_card).click()
        assert 'employment' in self.driver.current_url, "Nedošlo k přesměrování na kartu zaměstnance!"
        self.driver.find_element(*BaseChangePageLocators.dropdown_operation).click()

    def go_change(self):
        self.go()
        self.driver.find_element(*BaseChangePageLocators.dropdown_operation_item_change).click()
        assert 'new-amendment' in self.driver.current_url, "Nedošlo k přesměrování na 1. část formuláře pro vytvoření dodatku!"

    def go_cancel(self):
        self.go()
        self.driver.find_element(*BaseChangePageLocators.dropdown_operation_item_cancel).click()
        assert 'new-termination' in self.driver.current_url, "Nedošlo k přesměrování na formulář pro zrušení poměru!"

    def go_extend(self):
        self.go()
        self.driver.find_element(*BaseChangePageLocators.dropdown_operation_item_extend).click()
        assert 'employment-extension' in self.driver.current_url, "Nedošlo k přesměrování na formulář pro prodloužení poměru!"
