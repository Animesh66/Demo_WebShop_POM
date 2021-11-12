from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.utils_logging import Logger
import logging
from Utilities.utils_config_reader import configuration_reader
from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configuration_reader("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configuration_reader("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configuration_reader("locators", locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self, locator, value):

        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configuration_reader("locators", locator)).clear()
            self.driver.find_element_by_xpath(configuration_reader("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configuration_reader("locators", locator)).clear()
            self.driver.find_element_by_css_selector(configuration_reader("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configuration_reader("locators", locator)).clear()
            self.driver.find_element_by_id(configuration_reader("locators", locator)).send_keys(value)

        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))

    def select(self, locator, value):

        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element_by_xpath(configuration_reader("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element_by_css_selector(configuration_reader("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element_by_id(configuration_reader("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))

    def move_to(self, locator):

        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(configuration_reader("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(configuration_reader("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element_by_id(configuration_reader("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Moving to an element: " + str(locator))

    def verify_title(self, title):
        page_title = configuration_reader("page titles", title)
        assert page_title in self.driver.title, "Title of the page does not match"

    def explicit_wait_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(configuration_reader("locators", locator))
            wait.until(EC.element_to_be_clickable(element))
            element.click()
        elif str(locator).endswith("_CSS"):
            element =self.driver.find_element_by_css_selector(configuration_reader("locators", locator))
            wait.until(EC.element_to_be_clickable(element))
            element.click()
        elif str(locator).endswith("_ID"):
            element =self.driver.find_element_by_id(configuration_reader("locators", locator))
            wait.until(EC.element_to_be_clickable(element))
            element.click()


