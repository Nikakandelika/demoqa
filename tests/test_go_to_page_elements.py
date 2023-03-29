import time

from conftest import browser
from page.elements_page import ElementsPage
from page.demoqa import Demoqa


def test_go_to_page_elements(browser):
    el_page = ElementsPage(browser)
    demo_page = Demoqa(browser)

    demo_page.visit()
    assert demo_page.equal_url()
    # browser.execute_script('window.scrollBy(0, 100);', '#app > div > div > div.home-body > div > div:nth-child(1)')
    # time.sleep(5)
    demo_page.btn_elements.scroll_two_element()
    demo_page.btn_elements.click()
    assert el_page.equal_url()