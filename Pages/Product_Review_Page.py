from Pages.Base_Page import BasePage


class ProductReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_created_date(self):
        pass