from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки входа и регистрации на главной
    LOGIN_BUTTON_MAIN = By.XPATH, "//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"  # Кнопка "Личный кабинет"
    
    # Разделы конструктора
    BUNS_SECTION = By.XPATH, "//span[text()='Булки']"  # Раздел "Булки"
    SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']"  # Раздел "Соусы"
    FILLINGS_SECTION = By.XPATH, "//span[text()='Начинки']"  # Раздел "Начинки"
    
    # Активный раздел конструктора
    ACTIVE_SECTION = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]"
    
    # Логотип
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]"  # Логотип Stellar Burgers
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"  # Кнопка "Конструктор"

class RegistrationPageLocators:
    # Поля регистрации
    NAME_INPUT = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # Поле ввода имени
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/following-sibling::input"  # Поле ввода email
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"  # Поле ввода пароля
    
    # Кнопки
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"  # Кнопка регистрации
    LOGIN_LINK = By.XPATH, "//a[text()='Войти']"  # Ссылка "Войти" на странице регистрации
    
    # Сообщения об ошибках
    ERROR_MESSAGE = By.XPATH, "//p[contains(@class, 'input__error')]"  # Сообщение об ошибке

class LoginPageLocators:
    # Поля входа
    EMAIL_INPUT = By.XPATH, "//input[@type='text']"  # Поле ввода email
    PASSWORD_INPUT = By.XPATH, "//input[@type='password']"  # Поле ввода пароля
    
    # Кнопки
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"  # Кнопка "Войти"
    
    # Ссылки
    REGISTER_LINK = By.XPATH, "//a[text()='Зарегистрироваться']"  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = By.XPATH, "//a[text()='Восстановить пароль']"  # Ссылка восстановления пароля

class AccountPageLocators:
    # Кнопки в личном кабинете
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выйти']"  # Кнопка "Выйти"
    ORDER_HISTORY = By.XPATH, "//a[text()='История заказов']"  # История заказов

class CommonLocators:
    # Общие элементы
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"  # Кнопка "Оформить заказ" (признак авторизации)