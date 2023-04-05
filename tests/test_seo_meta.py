from page.demoqa import Demoqa
from page.alerts import Alerts
from page.accordian import Accordian
import pytest
import time

@pytest.mark.parametrize("pages", [Alerts, Demoqa, Accordian])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.meta.exist()
    assert page.meta.get_dom_attribute('name') == 'viewport'
    assert page.meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
