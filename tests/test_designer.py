from locators import Locators
buns="https://stellarburgers.nomoreparties.site/"
# Тест проверки перехода к разделу "Булки"
def test_go_to_the_rolls_section(driver):
    driver.get(buns)
    driver.find_element(*Locators.BUNS_SECTION_BUTTON).click()
    buns_header = driver.find_element(*Locators.BUNS_SECTION_HEADER)
    assert buns_header.is_displayed(), "Булки"

# Тест проверки перехода к разделу "Соусы"
def test_go_to_the_sauce_section(driver):
        driver.get(buns)
        driver.find_element(*Locators.SAUCES_SECTION_BUTTON).click()
        buns_header = driver.find_element(*Locators.SAUCES_SECTION_HEADER)
        assert buns_header.is_displayed(), "Соусы"

# Тест проверки перехода к разделу "Начинки"
def test_go_to_the_toppings_section(driver):
            driver.get(buns)
            driver.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
            buns_header = driver.find_element(*Locators.FILLINGS_SECTION_HEADER)
            assert buns_header.is_displayed(), "Начинки"