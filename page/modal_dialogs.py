from page.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }

        self.modal_dialogs = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_close_large_modal = WebElement (driver, '#closeLargeModal')
