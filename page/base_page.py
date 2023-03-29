from selenium.webdriver.common.by import By
import time
#методы и атрибуты страницы

class BasePage:
    def __init__(self, driver,base_url):
        self.driver = driver
        self.base_url = base_url  #'https://demoqa.com/'

    def visit(self):
        return self.driver.get(self.base_url)
#вставили в components
    # def find_element(self, locator):
    #     time.sleep(3)
    #     return self.driver.find_element(By.CSS_SELECTOR, locator)


    def back(self):
        self.driver.back()

    def forvard(self):
        self.driver.forvard()

    def refresh(self):
        self.driver.refresh()

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def get_title(self):
        return self.driver.title