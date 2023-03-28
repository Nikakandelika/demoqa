from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator="div.login_logo")
        except NoSuchElementException:
            return False
        return True
