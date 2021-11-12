from Pages.Base_Page import BasePage
from Pages.Home_Page import HomePage


class ProductReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_created_date(self):
        self.type("created_from_date_XPATH", "1/1/2017")
        self.type("created_to_date_XPATH", "12/11/2021")
        self.click("search_button_XPATH")

