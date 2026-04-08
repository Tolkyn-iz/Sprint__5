import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from test_data import TestUser
from locators import MainPageLocators, LoginPageLocators, CommonLocators  # ДОБАВИТЬ ИМПОРТЫ

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    # НЕ ОТКРЫВАЕМ ГЛАВНУЮ СТРАНИЦУ АВТОМАТИЧЕСКИ
    yield driver
    driver.quit()

# НОВЫЕ ФИКСТУРЫ ДЛЯ РАЗНЫХ СТРАНИЦ
@pytest.fixture
def driver_main_page(driver):
    """Фикстура для тестов, которым нужна главная страница"""
    driver.get("https://stellarburgers.education-services.ru")
    return driver

@pytest.fixture
def driver_login_page(driver):
    """Фикстура для тестов, которым нужна страница входа"""
    driver.get("https://stellarburgers.education-services.ru/login")
    return driver

@pytest.fixture
def driver_register_page(driver):
    """Фикстура для тестов, которым нужна страница регистрации"""
    driver.get("https://stellarburgers.education-services.ru/register")
    return driver

@pytest.fixture
def driver_account_page(driver):
    """Фикстура для тестов, которым нужна страница личного кабинета"""
    driver.get("https://stellarburgers.education-services.ru/account")
    return driver

@pytest.fixture
def driver_forgot_password_page(driver):
    """Фикстура для тестов, которым нужна страница восстановления пароля"""
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    return driver

@pytest.fixture
def authenticated_driver(driver, test_user_data):
    """Фикстура для авторизованного драйвера"""
    driver.get("https://stellarburgers.education-services.ru")
    
    # Выполняем вход
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(test_user_data["email"])
    
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user_data["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(CommonLocators.PLACE_ORDER_BUTTON)
    )
    
    return driver

@pytest.fixture
def registration_data():
    """Генерирует уникальные данные для регистрации"""
    from utils import generate_email, generate_password, generate_name
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password()
    }

@pytest.fixture
def test_user_data():
    """Фикстура с данными заранее созданного тестового пользователя"""
    return {
        "email": TestUser.VALID_USER["email"],
        "password": TestUser.VALID_USER["password"],
        "name": TestUser.VALID_USER["name"]
    }

@pytest.fixture
def new_user_data():
    """Фикстура с данными для регистрации нового пользователя"""
    return {
        "name": TestUser.NEW_USER["name"],
        "email": TestUser.NEW_USER["email"],
        "password": TestUser.NEW_USER["password"]
    }