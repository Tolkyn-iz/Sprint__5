import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators, CommonLocators
from utils import generate_invalid_password

class TestRegistration:
    
    def test_successful_registration(self, driver_main_page, new_user_data):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест успешной регистрации"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
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
        ).send_keys(new_user_data["name"])
        
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(new_user_data["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(new_user_data["password"])
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем, что после регистрации произошел переход на страницу входа
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
    
    def test_registration_with_empty_name(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест регистрации с пустым полем Имя"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Переход на страницу регистрации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        # Заполняем форму с пустым именем
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys("")  # Пустое поле Имя
        
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("test_empty_name@test.ru")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("ValidPass123")
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем появление сообщения об ошибке для пустого имени
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).text
        assert "имя" in error_message.lower() or "заполните" in error_message.lower()
    
    def test_registration_with_invalid_password(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест регистрации с некорректным паролем (менее 6 символов)"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
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
        
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("test_invalid@test.ru")
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