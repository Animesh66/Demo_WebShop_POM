import time

from Pages.Base_Page import BasePage
from Pages.Product_Review_Page import ProductReviewPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_product_review(self):
        self.click("catalog_XPATH")
        self.click("product_review_XPATH")
        # self.explicit_wait_clickable("catalog_XPATH")
        # self.explicit_wait_clickable("product_review_XPATH")
        return ProductReviewPage(self.driver)