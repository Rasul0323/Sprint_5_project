from locators import Locators

# Тест для входа по кнопке «Войти в аккаунт» на главной странице
def test_entrance_log_in_to_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("326758")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку "Личный кабинет"
def test_entrance_via_personal_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("326758")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку в форме регистрации
def test_entrance_via_the_log_in_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()

    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("326758")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку в форме восстановления пароля
def test_entrance_button_in_the_password_recovery_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*Locators.LOGIN_BUTTON_RECOVERY).click()

    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("rasul_sсhihveliev_18_693@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("326758")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()