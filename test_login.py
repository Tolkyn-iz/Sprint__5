import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, CommonLocators

class TestLogin:
    
    def test_login_via_main_button(self, driver_main_page, test_user_data):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Нажимаем кнопку "Войти в аккаунт" на главной
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)
        ).click()
        
        # Вводим данные заранее созданного пользователя
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(test_user_data["email"])
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user_data["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход (появление кнопки "Оформить заказ")
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_via_personal_account_button(self, driver_main_page, test_user_data):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест входа через кнопку 'Личный кабинет'"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Нажимаем кнопку "Личный кабинет"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Вводим данные заранее созданного пользователя
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(test_user_data["email"])
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user_data["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_via_registration_form(self, driver_register_page, test_user_data):  # ИЗМЕНИТЬ driver → driver_register_page
        """Тест входа через кнопку в форме регистрации"""
        driver = driver_register_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Нажимаем ссылку "Войти" на странице регистрации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()
        
        # Вводим данные заранее созданного пользователя
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(test_user_data["email"])
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user_data["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_via_forgot_password_form(self, driver_forgot_password_page, test_user_data):  # ИЗМЕНИТЬ driver → driver_forgot_password_page
        """Тест входа через кнопку в форме восстановления пароля"""
        driver = driver_forgot_password_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Нажимаем ссылку "Войти" на странице восстановления пароля
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()
        
        # Вводим данные заранее созданного пользователя
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(test_user_data["email"])
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user_data["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()