from page.text_box import TextBox

def test_placeholder(browser):
    text_page = TextBox(browser)
    text_page.visit()
    assert text_page.user_name.get_dom_attribute('placeholder') == 'Full Name'