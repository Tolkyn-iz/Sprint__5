import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, AccountPageLocators, CommonLocators

class TestPersonalAccount:
    
    def test_go_to_personal_account(self, authenticated_driver):  # ИСПОЛЬЗОВАТЬ authenticated_driver
        """Тест перехода в личный кабинет по клику на 'Личный кабинет'"""
        driver = authenticated_driver  # Уже авторизован и на главной
        
        # Нажимаем на "Личный кабинет"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Проверяем, что открылась страница личного кабинета
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AccountPageLocators.ORDER_HISTORY)
        )
        
        assert driver.find_element(*AccountPageLocators.ORDER_HISTORY).is_displayed()
    
    def test_go_from_account_to_constructor_by_button(self, authenticated_driver):
        """Тест перехода из личного кабинета в конструктор по клику на 'Конструктор'"""
        driver = authenticated_driver
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AccountPageLocators.ORDER_HISTORY)
        )
        
        # Нажимаем на "Конструктор"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        # Проверяем, что вернулись на главную (появилась кнопка "Оформить заказ")
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_go_from_account_to_constructor_by_logo(self, authenticated_driver):
        """Тест перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers"""
        driver = authenticated_driver
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AccountPageLocators.ORDER_HISTORY)
        )
        
        # Нажимаем на логотип
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        # Проверяем, что вернулись на главную
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
        )
        
        assert driver.find_element(*CommonLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_logout_from_account(self, authenticated_driver):
        """Тест выхода из аккаунта по кнопке 'Выйти' в личном кабинете"""
        driver = authenticated_driver
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AccountPageLocators.ORDER_HISTORY)
        )
        
        # Нажимаем кнопку "Выйти"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        ).click()
        
        # Проверяем, что перебросило на страницу входа
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()