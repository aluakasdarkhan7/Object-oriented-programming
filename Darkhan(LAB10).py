# ===== file_utils.py =====
# Содержит функции для работы с файлами

def read_file(file_path):
    """Чтение файла и вывод содержимого"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла:\n")
            print(content)
    except FileNotFoundError:
        print(f"❌ Ошибка: файл '{file_path}' не найден.")
    except IOError as e:
        print(f"❌ Ошибка при чтении файла: {e}")

def write_to_file(filename, text):
    """Записывает текст в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"✅ Текст успешно записан в {filename}")
    except IOError as e:
        print(f"❌ Ошибка при записи в файл: {e}")

def read_from_file(filename):
    """Чтение и вывод содержимого файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Содержимое файла '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"❌ Ошибка: файл '{filename}' не найден.")
# ===== exceptions_demo.py =====
# Содержит обработку стандартных и пользовательских исключений

class NegativeNumberError(Exception):
    """Пользовательское исключение для отрицательных чисел"""
    def __init__(self, number):
        super().__init__(f"❌ Ошибка: число {number} отрицательное! Введите положительное число.")

def divide_numbers():
    """Деление двух чисел с обработкой исключений"""
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a / b
    except ValueError:
        print("❌ Ошибка: введено не число.")
    except ZeroDivisionError:
        print("❌ Ошибка: деление на ноль невозможно.")
    else:
        print(f"Результат деления: {result}")
    finally:
        print("🔹 Программа завершена.")

def check_positive(number):
    """Проверка числа на положительность"""
    if number < 0:
        raise NegativeNumberError(number)
    print(f"✅ Число {number} корректно!")
# ===== main.py =====
# Главный скрипт для демонстрации всех задач

from file_utils import read_file, write_to_file, read_from_file
from exceptions_demo import divide_numbers, check_positive, NegativeNumberError

def task_files_demo():
    print("\n=== TASK 1 & 2: Работа с файлами ===")
    sample_file = "sample.txt"
    example_file = "example.txt"
    
    # Task 1: Чтение файла
    read_file(sample_file)
    
    # Task 2: Запись и чтение файла
    text = "Ernur Esimuly"
    write_to_file(example_file, text)
    read_from_file(example_file)

def task_exceptions_demo():
    print("\n=== TASK 3: Исключения при делении ===")
    divide_numbers()
    
    print("\n=== TASK 4: Пользовательское исключение ===")
    try:
        num = float(input("Введите число: "))
        check_positive(num)
    except ValueError:
        print("❌ Ошибка: введено не число.")
    except NegativeNumberError as e:
        print(e)

if __name__ == "__main__":
    task_files_demo()
    task_exceptions_demo()
