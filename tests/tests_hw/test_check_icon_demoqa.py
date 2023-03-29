from page.demoqa import Demoqa


def test_icon_exist(browser):
    browser.get('https://demoqa.com/')
    icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")

    if icon is None:
        print('Элемент не найден')
    else:
        print("Элементы найдены")


def test_icon_exist(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()

    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()