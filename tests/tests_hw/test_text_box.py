from page.text_box import TextBox
import time
def text_boxx(browser):
    name = 'Nika'
    address = 'SPb'
    text_box1 = TextBox(browser)
    text_box1.visit()

    text_box1.user_name.send_keys(name)
    text_box1.current_address.send_keys(address)

    text_box1.btn_submit.click_force()
    time.sleep(3)
    assert text_box1.footer_name.get_text() == f'Name:{name}'
    assert text_box1.footer_address.get_text() == f'Current Address:{address}'
