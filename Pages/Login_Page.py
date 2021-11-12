from Pages.Base_Page import BasePage
from Pages.Home_page import HomePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def perform_login(self, email, password):
        self.type("email_ID", email)
        self.type("password_ID", password)
        self.click("login_button_XPATH")
        self.verify_title("home_page_title")
        return HomePage(self.driver)

