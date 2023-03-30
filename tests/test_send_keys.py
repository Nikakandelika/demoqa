import time
from page.form_page import FormPage

def test_send_keys(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('Veronika')
    form_page.last_name.send_keys('Dubrova')
    form_page.user_email.send_keys('vdubrova@gmail.com')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('89273396882')


    form_page.hobbies.click_force()
    form_page.current_address.send_keys('Hello')
    form_page.btn_submit.click_force()

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()