import allure
@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():
    assert 111 == 222