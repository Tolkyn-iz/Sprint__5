import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators, CommonLocators
from utils import generate_invalid_password

class TestRegistration:
    
    def test_successful_registration(self, driver, registration_data):
        """Тест успешной регистрации"""
        # Нажимаем на кнопку "Личный кабинет" для перехода к регистрации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Нажимаем на ссылку "Зарегистрироваться"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        # Заполняем форму регистрации
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys(registration_data["name"])
        
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(registration_data["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(registration_data["password"])
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем, что после регистрации произошел переход на страницу входа
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
    
    def test_registration_with_invalid_password(self, driver):
        """Тест регистрации с некорректным паролем (менее 6 символов)"""
        # Переход на страницу регистрации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        # Заполняем форму с коротким паролем
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys("Тестовый Пользователь")
        
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("test@test.ru")
        invalid_password = generate_invalid_password()
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(invalid_password)
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем появление сообщения об ошибке
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).text
        assert "Некорректный пароль" in error_message or "пароль" in error_message.lower()