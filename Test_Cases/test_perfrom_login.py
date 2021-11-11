import pytest
from Pages.Login_Page import LoginPage
from Test_Cases.Base_Test import BaseTest
from Utilities.data_provider import get_data


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email, password", get_data("sheet_name"))
    def test_perform_login(self, email, password):
        login = LoginPage(self.driver)
        login.perform_login(email, password)



