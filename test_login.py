import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, CommonLocators

class TestLogin:
    
    @pytest.fixture(autouse=True)
    def create_user(self, driver, registration_data):
        """Фикстура для создания пользователя перед тестами входа"""
        # Регистрируем пользователя
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys(registration_data["name"])
        
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(registration_data["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(registration_data["password"])
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Сохраняем данные пользователя для входа
        self.user_email = registration_data["email"]
        self.user_password = registration_data["password"]
        
        # Возвращаемся на главную
        driver.get("https://stellarburgers.education-services.ru")
    
    def test_login_via_main_button(self, driver):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        # Нажимаем кнопку "Войти в аккаунт" на главной
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)
        ).click()
        
        # Вводим данные
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(self.user_email)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.user_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход (появление кнопки "Оформить заказ")
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_via_personal_account_button(self, driver):
        """Тест входа через кнопку 'Личный кабинет'"""
        # Нажимаем кнопку "Личный кабинет"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Вводим данные
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(self.user_email)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.user_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_via_registration_form(self, driver):
        """Тест входа через кнопку в форме регистрации"""
        # Переходим в личный кабинет
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Переходим на страницу регистрации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        # Нажимаем ссылку "Войти" на странице регистрации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()
        
        # Вводим данные
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(self.user_email)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.user_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_via_forgot_password_form(self, driver):
        """Тест входа через кнопку в форме восстановления пароля"""
        # Переходим в личный кабинет
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Переходим на страницу восстановления пароля
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        ).click()
        
        # Нажимаем ссылку "Войти" на странице восстановления пароля
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Вводим данные
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(self.user_email)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.user_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()