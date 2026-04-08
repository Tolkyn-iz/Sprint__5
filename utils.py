import random
import string

def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_номер_когорты_3цифры@домен"""
    first_names = ['alex', 'ivan', 'maria', 'elena', 'dmitry', 'olga', 'sergey', 'anna']
    last_names = ['testov', 'petrov', 'sidorov', 'smirnov', 'kuznetsov', 'popov']
    cohort = random.randint(1, 10)
    random_digits = ''.join(random.choices(string.digits, k=3))
    domains = ['yandex.ru', 'mail.ru', 'gmail.com', 'ya.ru']
    
    name = random.choice(first_names)
    last = random.choice(last_names)
    domain = random.choice(domains)
    
    email = f"{name}_{last}_{cohort}_{random_digits}@{domain}"
    return email

def generate_password(min_length=6):
    """Генерирует пароль указанной длины"""
    length = random.randint(min_length, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_name():
    """Генерирует случайное имя"""
    names = ['Александр', 'Мария', 'Дмитрий', 'Елена', 'Сергей', 'Анна', 'Максим', 'Екатерина']
    return random.choice(names)

def generate_invalid_password():
    """Генерирует короткий пароль (менее 6 символов) для проверки ошибки"""
    length = random.randint(1, 5)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))