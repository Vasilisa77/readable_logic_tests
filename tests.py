from datetime import time


def test_dark_theme_by_time():
    """
    Проверяет переключение темной темы в зависимости от времени (с 22:00 до 06:00).
    """
    current_time = time(hour=23)

    # Логика: тема включена, если час >= 22 или < 6
    is_dark_theme = current_time.hour >= 22 or current_time.hour < 6

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Проверяет приоритет выбора темы:
    - Если пользователь выбрал тему вручную (True/False), используется его выбор.
    - Если выбор пользователя не задан (None), тема зависит от времени (с 22 до 06).
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = current_time.hour >= 22 or current_time.hour < 6

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Находит пользователей в списке по заданным критериям:
    - Поиск пользователя по имени "Olga"
    - Поиск всех пользователей младше 20 лет
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Находим пользователя с именем "Olga"
    suitable_user = next(user for user in users if user["name"] == "Olga")
    assert suitable_user == {"name": "Olga", "age": 45}

    # Находим всех пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def get_readable_name(func, *args):
    """
    Преобразует имя функции из snake_case в Title Case и форматирует аргументы.
    Пример: open_browser -> "Open Browser [Chrome]"
    """
    func_name = func.__name__.replace('_', ' ').title()
    arg_values = ", ".join(args)

    result = f"{func_name} [{arg_values}]"
    print(result)
    return result


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = get_readable_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = get_readable_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = get_readable_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


if __name__ == "__main__":
    print("--- Запуск тестов форматирования функций ---")
    test_readable_function()

    print("\n--- Запуск тестов поиска пользователей ---")
    test_find_suitable_user()

    print("--- Запуск тестов темной темы ---")
    test_dark_theme_by_time()
    test_dark_theme_by_time_and_user_choice()

    print("\nПОЗДРАВЛЯЮ! Все тесты успешно пройдены! 🌟")
    