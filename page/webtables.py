from page.base_page import BasePage
from components.components import WebElement
class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.pageData = {
            "title": "DEMOQA"
        }

        self.user_form = WebElement(driver, '#userForm')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.age = WebElement(driver, '#age')
        self.email = WebElement(driver, '#userEmail')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_pencil = WebElement(driver, '#edit-record-4 > svg')
        self.first_name_in_tables = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')

        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.title_delete = WebElement(driver, '[title="Delete"')
#дз 12 задание 3
        self.first_name_table = WebElement(driver, '')
        self.last_name_table = WebElement(driver, '')
        self.age_table = WebElement(driver, '')
        self.email_table = WebElement(driver, '')
        self.salary_table = WebElement(driver, '')
        self.department_table = WebElement(driver, '')



