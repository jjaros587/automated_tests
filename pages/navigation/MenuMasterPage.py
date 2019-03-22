from pages.BasePage import BasePage


class MenuMasterPage(BasePage):

    def verify_page(self, driver, item):
        assert item['locator'] in driver.current_url, "Nedošlo k přesměrování na stránku " + item['link']
        super().verify_page_status_code(driver)