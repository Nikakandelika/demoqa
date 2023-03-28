
from page.swag_labs import SwagLabs

def test_icon_exist(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    swag_labs.exist_icon()

