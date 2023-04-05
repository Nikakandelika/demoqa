from page.webtables import WebTables
import time
import allure

#дома 1
@allure.title('Проверка блока Webtables')
def test_webtables_home(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()
    web_tables_page.btn_add.click()
    assert web_tables_page.user_form.visible()
    web_tables_page.btn_submit.click()
    assert web_tables_page.user_form.get_dom_attribute('class') == 'was-validated'

    web_tables_page.first_name.send_keys('Nika')
    web_tables_page.last_name.send_keys('Lazareva')
    web_tables_page.email.send_keys('Nika@mail.ru')
    web_tables_page.age.send_keys('66')
    web_tables_page.salary.send_keys('200000')
    web_tables_page.department.send_keys('testing')

    web_tables_page.btn_submit.click()
    time.sleep(2)
    assert web_tables_page.first_name_in_tables.get_text() == 'Nika'

    web_tables_page.btn_pencil.click()
    assert web_tables_page.first_name_in_tables.visible()
    assert web_tables_page.first_name.get_dom_attribute('value') == 'Nika'

    web_tables_page.first_name.clear()
    web_tables_page.first_name.send_keys('Veronika')
    web_tables_page.btn_submit.click()
    assert not web_tables_page.first_name_in_tables.get_text() == 'Nika'


#дома 2
# def test_web_tables_home(browser):
#     web_tables = WebTables
#     web_tables.visit()


#в классе
@allure.title('удаление из таблицы')
def test_webtable(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert not web_tables.no_rows_found.exist()

    #удаляем все записи
    while web_tables.title_delete.exist():
        web_tables.title_delete.click()

    time.sleep(2)
    assert web_tables.no_rows_found.exist()

