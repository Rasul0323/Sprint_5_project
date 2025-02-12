from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест проверки перехода по клику на «Личный кабинет»
def test_click_to_your_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'