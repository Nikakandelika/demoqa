from page.alerts import Alerts
import time

def test_check_alert(browser):
    check_alert = Alerts(browser)
    check_alert.visit()

    check_alert.btn_timer_alert.click()
    time.sleep(5)
    assert check_alert.alert()