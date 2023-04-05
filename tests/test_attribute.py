from page.text_box import TextBox
import allure
@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.BLOCKER)

def test_placeholder(browser):
    text_page = TextBox(browser)
    text_page.visit()
    assert text_page.user_name.get_dom_attribute('placeholder') == 'Full Name'
