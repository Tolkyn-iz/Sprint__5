import time
import pytest
from selenium.webdriver.common.by import By  # ДОБАВИТЬ ЭТУ СТРОКУ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestConstructor:
    
    def test_switch_to_buns_section(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест перехода к разделу 'Булки'"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Переключаемся на другой раздел, чтобы потом вернуться
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()
        time.sleep(1)
        
        # Переключаемся обратно на "Булки"
        driver.find_element(*MainPageLocators.BUNS_TAB).click()
        time.sleep(1)
        
        # Способ 1: Проверяем через aria-selected атрибут
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB_ARIA)
        active_tab_text = active_tab.find_element(By.XPATH, ".//span").text
        assert active_tab_text == "Булки", f"Активный таб должен быть 'Булки', получен '{active_tab_text}'"
    
    def test_switch_to_sauces_section(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест перехода к разделу 'Соусы'"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Нажимаем на раздел "Соусы"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()
        
        time.sleep(1)
        
        # Способ 2: Проверяем через динамический локатор
        active_tab = driver.find_element(*MainPageLocators.get_active_tab_by_text("Соусы"))
        assert active_tab.is_displayed(), "Таб 'Соусы' должен быть активным"
    
    def test_switch_to_fillings_section(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест перехода к разделу 'Начинки'"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Нажимаем на раздел "Начинки"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        ).click()
        
        time.sleep(1)
        
        # Способ 3: Проверяем через JavaScript (самый надежный)
        is_active = driver.execute_script("""
            const tabs = document.querySelectorAll('[role="tab"]');
            for (let tab of tabs) {
                if (tab.getAttribute('aria-selected') === 'true' && 
                    tab.innerText.includes('Начинки')) {
                    return true;
                }
            }
            return false;
        """)
        
        assert is_active, "Раздел 'Начинки' должен быть активным"
    
    def test_switch_to_buns_section_alternative(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Альтернативный тест: проверка через видимый контент"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Переключаемся на "Соусы", потом обратно на "Булки"
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        time.sleep(1)
        driver.find_element(*MainPageLocators.BUNS_TAB).click()
        time.sleep(1)
        
        # Проверяем, что контент с булками видим
        buns_content = driver.find_element(By.XPATH, "//div[contains(@class, 'tab-content')]//h2[text()='Булки']")
        assert buns_content.is_displayed(), "Контент с булками должен быть видимым"
        
        # Проверяем, что контент с соусами скрыт
        sauces_content = driver.find_element(By.XPATH, "//div[contains(@class, 'tab-content')]//h2[text()='Соусы']")
        assert not sauces_content.is_displayed() or sauces_content.get_attribute("style") == "display: none;", \
            "Контент с соусами должен быть скрыт"

class TestConstructorRobust:
    """Класс с максимально надежными тестами, устойчивыми к изменениям верстки"""
    
    def test_tab_activation_by_attribute(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест проверки активации таба через стандартные атрибуты"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        # Кликаем по каждому табу и проверяем aria-selected
        tabs = [
            ("Булки", MainPageLocators.BUNS_TAB),
            ("Соусы", MainPageLocators.SAUCES_TAB),
            ("Начинки", MainPageLocators.FILLINGS_TAB)
        ]
        
        for tab_name, tab_locator in tabs:
            # Кликаем по табу
            driver.find_element(*tab_locator).click()
            time.sleep(1)
            
            # Находим активный таб по aria-selected
            active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB_ARIA)
            active_text = active_tab.find_element(By.XPATH, ".//span").text
            
            assert active_text == tab_name, \
                f"После клика на '{tab_name}', активным должен быть '{tab_name}', получен '{active_text}'"
    
    def test_content_visibility(self, driver_main_page):  # ИЗМЕНИТЬ driver → driver_main_page
        """Тест проверки, что при клике на таб меняется видимое содержимое"""
        driver = driver_main_page  # ДОБАВИТЬ ЭТУ СТРОКУ
        sections = {
            "Булки": "//h2[text()='Булки']",
            "Соусы": "//h2[text()='Соусы']",
            "Начинки": "//h2[text()='Начинки']"
        }
        
        for section_name, content_xpath in sections.items():
            # Находим и кликаем по табу
            tab = driver.find_element(By.XPATH, f"//span[text()='{section_name}']/parent::div")
            tab.click()
            time.sleep(1)
            
            # Проверяем, что нужный контент стал видимым
            content = driver.find_element(By.XPATH, content_xpath)
            assert content.is_displayed(), f"Контент '{section_name}' должен быть видимым"