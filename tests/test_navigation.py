from page.demoqa import Demoqa
from page.elements_page import ElementsPage
def test_navigation(browser):
    page_object = Demoqa(browser)
    elements_page = ElementsPage(browser)

    page_object.visit()
    page_object.btn_elements.click()

    page_object.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()



