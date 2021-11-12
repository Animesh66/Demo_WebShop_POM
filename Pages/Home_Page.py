from Pages.Base_Page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_product_review(self):
        self.click("catalog_XPATH")
        self.click("product_review_XPATH")