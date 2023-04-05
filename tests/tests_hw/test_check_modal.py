from page.modal_dialogs import ModalDialogs
import time
def test_check_modal(browser):
    check_modal = ModalDialogs(browser)
    check_modal.visit()

    check_modal.btn_small_modal.click()
    time.sleep(2)
    check_modal.alert()
    check_modal.btn_close_small_modal.click()

    check_modal.btn_large_modal.click()
    time.sleep(2)
    check_modal.alert()
    check_modal.btn_close_large_modal.click()
#доработать, чтобы тест работал, если страница недоступна



