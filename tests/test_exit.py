from conftest import login
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест выхода по кнопке «Выйти» в личном кабинете.
def test_exit_using_the_exit_button(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.SIGN_OUT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'