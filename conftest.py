import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

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
    
    driver.get("https://stellarburgers.education-services.ru")
    yield driver
    driver.quit()

@pytest.fixture
def registration_data():
    """Генерирует уникальные данные для регистрации"""
    from utils import generate_email, generate_password, generate_name
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password()
    }