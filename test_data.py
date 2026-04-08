# test_data.py

class TestUser:
    """Класс с данными тестового пользователя"""
    
    # Данные существующего тестового пользователя
    VALID_USER = {
        "name": "Тестовый Пользователь",
        "email": "test_user@example.com",
        "password": "ValidPass123"
    }
    
    # Альтернативный тестовый пользователь (на случай блокировки)
    BACKUP_USER = {
        "name": "Резервный Пользователь",
        "email": "backup_user@example.com",
        "password": "BackupPass456"
    }
    
    # Данные для регистрации нового пользователя (если нужно)
    NEW_USER = {
        "name": "Новый Пользователь",
        "email": "new_user@example.com",
        "password": "NewPass789"
    }