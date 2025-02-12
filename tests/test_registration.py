from locators import Locators


# Тест проверки успешной регистрации
def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_INPUT).send_keys("Расул")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("326758")
    driver.find_element(*Locators.SUBMIT_BUTTON).click()
    success_message = driver.find_element(*Locators.SUCCESS_MESSAGE).text

    assert "Зарегистрироваться" in success_message

# Тест для проверки ошибки для некорректного пароля
def test_password_error(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.NAME_INPUT).send_keys("Расул")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("285")
    driver.find_element(*Locators.SUBMIT_BUTTON).click()
    error_message = driver.find_element(*Locators.PASSWORD_ERROR).text

    assert "Некорректный пароль" in error_message