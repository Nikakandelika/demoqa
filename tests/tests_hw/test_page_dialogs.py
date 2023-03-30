from page.modal_dialogs import ModalDialogs
from page.demoqa import Demoqa
def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    assert modal_elements.modal_dialogs.check_count_elements(5)

def test_navigation_modal(browser):
    navigation_modal = ModalDialogs(browser)
    demoqa_page = Demoqa(browser)
    navigation_modal.visit()
    navigation_modal.refresh()

    navigation_modal.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert demoqa_page.equal_url()
    # assert demoqa_page.title()

    browser.set_window_size(1000, 1000)

