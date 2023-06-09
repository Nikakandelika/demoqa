from page.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

#храним атрибуты как элементы на странице

class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)' )
        self.footer_text = WebElement(driver, '#app > footer > span')
        self.title = WebElement(driver, 'head > title')
    # def exist_icon(self):
    #     try:
    #         self.icon.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     self.find_element(locator='#app > header > a').click()
    #
    # def click_on_the_btn(self):
    #     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

    # def equal_url(self):
    #    if self.get_url() == self.base_url():
    #        return True
    #    return False


class DemoQa:
    pass