from page.browser_tab import BrowserTab
import allure
import time


@allure.title('Проверка ...')
def test_browser_tab(browser):
    browser_tab = BrowserTab(browser)
    browser_tab.visit()
    assert len(browser.window_handles) == 1
    browser_tab.new_tab.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    assert browser_tab.get_url() == 'https://demoqa.com/browser-windows'

