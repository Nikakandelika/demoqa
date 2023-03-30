from page.elements_page import ElementsPage
import time
def test_visible_btn_sidebar(browser):
    page_element = ElementsPage(browser)

    page_element.visit()
    # page_element.btn_sidebar_first.click()
    # time.sleep(3)
    # assert page_element.btn_sidebar_first_textbox.exist()
    assert page_element.btn_sidebar_first_textbox.visible()
def test_not_visible_btn_sidebar(browser):
    page_element1 = ElementsPage(browser)
    page_element1.visit()
    assert page_element1.btn_sidebar_first_checkbox.visible()
    page_element1.btn_sidebar_first.click()
    time.sleep(3)
    assert not page_element1.btn_sidebar_first_checkbox.visible()

