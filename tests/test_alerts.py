from page.alerts import Alerts
import time
import allure
@allure.title('Проверка видимости алерта')
def test_alerts(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()
    assert not alerts_page.alert()
    alerts_page.btn_alert.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()
def test_alert_text(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()
def test_confirm(browser):
    confirm_page = Alerts(browser)
    confirm_page.visit()
    confirm_page.btn_confirm.click()
    time.sleep(2)
    confirm_page.alert().dismiss()
    assert confirm_page.confirm_result.get_text() == 'You Selected Cancel'

def test_prompt(browser):
    name = 'Nika'
    prompt_page = Alerts(browser)
    prompt_page.visit()
    prompt_page.btn_prompt.click()
    time.sleep(2)
    prompt_page.alert().send_keys(name)
    prompt_page.alert().accept()
    assert prompt_page.prompt_result.get_text() == f'You entered {name}'
    time.sleep(2)

