from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import login
from locators import Locators


# Тест проверки перехода по клику на «Конструктор»
def test_transition_to_constructor_via_button(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# Тест проверки перехода по клику на логотип Stellar Burgers
def test_transition_to_constructor_via_logo(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.LOGO_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'