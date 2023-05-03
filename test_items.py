import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_basket_exist(browser):
    browser.get(link)
    time.sleep(3)
    btn_add_to_basket = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert btn_add_to_basket > 0, 'btn_add_to_basket is not exist'

