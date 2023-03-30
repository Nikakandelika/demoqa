from page.modal_dialogs import ModalDialogs
import time
def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    # modal_elements.modal_dialogs.elements_count(5)

def test_navigation_modal(browser):
    navigation_modal = ModalDialogs(browser)
    navigation_modal.visit()
    navigation_modal.refresh()

    navigation_modal.icon()
    navigation_modal.back()

    browser.set_window_size(900, 400)
    time.sleep(2)
    navigation_modal.forvard()

    assert navigation_modal.equal_url()
    assert navigation_modal.get_title()

    browser.set_window_size(1000, 1000)

