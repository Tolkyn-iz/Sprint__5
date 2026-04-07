import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestConstructor:
    
    def test_switch_to_buns_section(self, driver):
        """Тест перехода к разделу 'Булки'"""
        # Проверяем, что раздел "Булки" активен по умолчанию
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        
        # Переключаемся на другой раздел, чтобы потом вернуться
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        time.sleep(1)
        
        # Переключаемся обратно на "Булки"
        driver.find_element(*MainPageLocators.BUNS_SECTION).click()
        time.sleep(1)
        
        # Проверяем, что раздел "Булки" стал активным
        active_section = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        assert "Булки" in active_section.text
    
    def test_switch_to_sauces_section(self, driver):
        """Тест перехода к разделу 'Соусы'"""
        # Нажимаем на раздел "Соусы"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        ).click()
        
        time.sleep(1)
        
        # Проверяем, что раздел "Соусы" стал активным
        active_section = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        assert "Соусы" in active_section.text
    
    def test_switch_to_fillings_section(self, driver):
        """Тест перехода к разделу 'Начинки'"""
        # Нажимаем на раздел "Начинки"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        ).click()
        
        time.sleep(1)
        
        # Проверяем, что раздел "Начинки" стал активным
        active_section = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        assert "Начинки" in active_section.text