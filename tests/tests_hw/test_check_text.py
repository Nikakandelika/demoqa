from conftest import browser
from page.elements_page import ElementsPage
from page.demoqa import Demoqa


def test_go_to_page_elements(browser):
    el_page = ElementsPage(browser)
    demo_page = Demoqa(browser)

    demo_page.visit()
    assert demo_page.equal_url()

    demo_page.btn_elements.scroll_two_element()
    demo_page.btn_elements.click()
    assert el_page.equal_url()


def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == "Elements"

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()
