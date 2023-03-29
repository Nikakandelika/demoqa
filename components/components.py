
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#отдельный файл, без наследования , в котором хранятся методы


class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def get_text(self):
        return str(self.find_element().text)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def scroll_two_element(self):
        self.driver.execute_script('window.scrollBy(0, 100);', '#app > div > div > div.home-body > div > div:nth-child(1)')

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        else:
            return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)







