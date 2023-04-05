from page.demoqa import Demoqa
from page.alerts import Alerts
import pytest
import time
def test_seo(browser):
    seo_page = Demoqa(browser)
    seo_page.visit()
    assert browser.title == seo_page.pageData['title']

@pytest.mark.parametrize("pages", [Alerts, Demoqa])
def test_check_title_all_pages(browser, pages):
    page_demo = pages(browser)
    page_demo.visit()
    time.sleep(2)
    assert browser.title == page_demo.pageData['title']

