from Test_Cases.Base_Test import BaseTest
import pytest
from Utilities.data_provider import get_data


class TestVerifyProductReview(BaseTest):

    @pytest.mark.parametrize("created_from_date, created_to_date", get_data("sheet_name"))
    def test_verify_product_review(self, created_from_date, created_to_date):
        pass