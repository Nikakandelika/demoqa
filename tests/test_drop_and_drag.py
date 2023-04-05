from selenium.webdriver import ActionChains
from page.droppable import Droppable
import time

def test_drag_and_drop(browser):
    action_chains = ActionChains(browser)
    drop_page = Droppable(browser)

    drop_page.visit()
    # assert not drop_page.drop.check_css('backgroundColor', 'steelblue')
    action_chains.drag_and_drop(drop_page.drag.find_element(), drop_page.drop.find_element()).perform()
    time.sleep(1)
    assert drop_page.drop.check_css('backgroundColor', 'steelblue')
    action_chains.drag_and_drop(drop_page.drop.find_element(), drop_page.area.find_element()).perform()
    assert drop_page.drop.check_css('backgroundColor', 'steelblue')




