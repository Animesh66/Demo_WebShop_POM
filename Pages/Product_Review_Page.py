from Pages.Base_Page import BasePage
from Pages.Home_Page import HomePage


class ProductReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_reviews(self, created_from_date, created_to_date):
        self.type("created_from_date_XPATH", created_from_date)
        self.type("created_to_date_XPATH", created_to_date)
        self.click("search_button_XPATH")

