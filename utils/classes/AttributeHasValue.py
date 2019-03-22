class AttributeHasValue:
    def __init__(self, locator, attribute, value):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        return self.value in driver.find_element(self.locator).get_attribute(self.attribute)