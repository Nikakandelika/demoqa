from page.base_page import BasePage
from components.components import WebElement
class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'

        super().__init__(driver, self.base_url)

        self.pageData = {
            'title': 'DEMOQA'
        }

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')

