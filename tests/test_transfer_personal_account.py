from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'
# Тест проверки перехода по клику на «Личный кабинет»
def test_click_to_your_personal_account(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(LOGIN_PAGE_URL))

    assert driver.current_url == LOGIN_PAGE_URL