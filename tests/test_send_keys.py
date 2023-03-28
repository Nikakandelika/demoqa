from page.form_page import FormPage
import time
def test_send_keys(browser):
    send_keys = FormPage(browser)
    send_keys.visit()
    send_keys.first_name.send_keys('Nika')
    time.sleep(3)