from pages.base_page import BasePage
from components.components import WebElement


class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }
        self.text_elements = WebElement(driver, '#section1Content > p')
        self.btn_elements = WebElement(driver, '#section1Heading')

        self.text_elements1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.text_elements2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.text_elements3 = WebElement(driver, '#section3Content > p')