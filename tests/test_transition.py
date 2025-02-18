from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import login
from locators import Locators
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL

# Тест проверки перехода по клику на «Конструктор»
def test_transition_to_constructor_via_button(driver, login):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(MAIN_PAGE_URL))

    assert driver.current_url == MAIN_PAGE_URL


# Тест проверки перехода по клику на логотип Stellar Burgers
def test_transition_to_constructor_via_logo(driver, login):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(*Locators.LOGO_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(MAIN_PAGE_URL))

    assert driver.current_url == MAIN_PAGE_URL