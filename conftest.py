import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locators
from urls import LOGIN_PAGE_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("326758")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    yield