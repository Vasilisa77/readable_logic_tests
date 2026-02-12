from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    # Если час больше или равен 22 ИЛИ меньше 6 — значит сейчас ночь и нужна темная тема
    if current_time.hour >= 22 or current_time.hour < 6:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    # TODO переключите темную тему в зависимости от времени суток,
    # но учтите что темная тема может быть включена вручную

    # Логика: если пользователь явно выбрал тему (не None), используем его выбор.
    # Если пользователь ничего не выбирал (None), то проверяем по времени.
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = current_time.hour >= 22 or current_time.hour < 6

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    # Проходим по списку и берем того, у кого имя совпадает
    suitable_users = next(user for user in users if user["name"] == "Olga")
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    # Создаем новый список только с теми, кто младше 20
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def get_readable_name(func, *args):
    # Преобразуем имя функции: меняем '_' на пробел и делаем слова с заглавной буквы
    func_name = func.__name__.replace('_', ' ').title()
    # Объединяем аргументы в строку через запятую
    arg_values = ", ".join(args)
    # Формируем итоговую строку
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