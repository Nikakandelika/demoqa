import time
from page.text_box import TextBox

def test_clear(browser):
    clear_page = TextBox(browser)
    clear_page.visit()
    clear_page.user_name.send_keys('Hello')
    time.sleep(2)
    clear_page.user_name.clear()
    time.sleep(2)
    assert clear_page.user_name.get_text() == ''