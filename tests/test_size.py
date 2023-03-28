from page.demoqa import Demoqa
import time
def test_size(browser):
    size_page = Demoqa(browser)
    size_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

