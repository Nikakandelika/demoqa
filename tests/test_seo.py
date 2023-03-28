from page.demoqa import Demoqa

def test_seo(browser):
    seo_page = Demoqa(browser)
    seo_page.visit()
    assert browser.title == seo_page.pageData['title']
