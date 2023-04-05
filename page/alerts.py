from page.base_page import BasePage
from components.components import WebElement
class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }

        self.btn_alert = WebElement(driver, '#alertButton')
        self.confirm_result = WebElement(driver, '#confirmResult')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.btn_prompt = WebElement(driver, '#promptButton')
        self.btn_timer_alert = WebElement(driver, '#timerAlertButton')
        self.prompt_result = WebElement(driver, '#promptResult')

