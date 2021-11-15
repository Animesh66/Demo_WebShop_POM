import time

from Pages.Login_Page import LoginPage
from Test_Cases.Base_Test import BaseTest
import pytest
from Utilities.data_provider import get_data


class TestVerifyProductReview(BaseTest):

    @pytest.mark.parametrize("email, password, created_from_date, created_to_date", get_data("sheet_name"))
    def test_verify_product_review(self, email, password, created_from_date, created_to_date):
        login = LoginPage(self.driver)
        # login.perform_login(email, password).navigate_product_review()
        login.perform_login(email, password).navigate_product_review().search_reviews_input(created_from_date,
                                                                                            created_to_date)
