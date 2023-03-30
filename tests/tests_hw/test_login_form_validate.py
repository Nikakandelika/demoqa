import time
from page.form_page import FormPage

def test_login_form_validate(browser):
    text_login_form = FormPage(browser)
    text_login_form.visit()
#b:
    assert text_login_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert text_login_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert text_login_form.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    # assert text_login_form.user_email.get_dom_attribute('pattern') == ''
#c:
    text_login_form.btn_submit.click_force()
    time.sleep(3)
    assert text_login_form.user_form.get_dom_attribute('class') == 'was-validated'