from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки входа и регистрации на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Разделы конструктора (сами элементы табов)
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Альтернативный вариант: локаторы для самих кнопок-табов
    BUNS_TAB_BUTTON = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Булки']")
    SAUCES_TAB_BUTTON = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Соусы']")
    FILLINGS_TAB_BUTTON = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Начинки']")
    
    # Способ 1: Проверка через атрибут aria-selected (наиболее надежный)
    ACTIVE_TAB_ARIA = (By.XPATH, "//div[@role='tab' and @aria-selected='true']")
    
    # Способ 2: Проверка через disabled атрибут (если активный таб disabled)
    ACTIVE_TAB_DISABLED = (By.XPATH, "//div[@role='tab' and @disabled]")
    
    # Способ 3: Проверка через data-атрибут (если есть)
    ACTIVE_TAB_DATA = (By.XPATH, "//div[@data-tab='active']")
    
    # Способ 4: Проверка через видимость/положение (если активный контент видим)
    ACTIVE_CONTENT = (By.XPATH, "//div[contains(@class, 'tab-content') and not(contains(@style, 'display: none'))]")
    
    # Способ 5: Комбинированный - ищем таб, связанный с видимым контентом
    ACTIVE_TAB_BY_CONTENT = (By.XPATH, "//div[@role='tabpanel' and not(contains(@style, 'display: none'))]/preceding-sibling::div[@role='tab']")
    
    # Логотип и навигация
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    
    # Дополнительно: локатор для проверки активного таба через сравнение с текстом
    @staticmethod
    def get_active_tab_by_text(expected_text):
        """Динамический локатор для активного таба с определенным текстом"""
        return (By.XPATH, f"//div[@role='tab' and @aria-selected='true']//span[text()='{expected_text}']")

class RegistrationPageLocators:
    # Поля регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопки
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    
    # Сообщения об ошибках
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")

class LoginPageLocators:
    # Поля входа
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылки
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class AccountPageLocators:
    # Кнопки в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")

class CommonLocators:
    # Общие элементы
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")