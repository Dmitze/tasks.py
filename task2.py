import os

def total_salary(path):
    """
    Обчислює загальну та середню зарплату, читаючи дані з текстового файлу.
    Обробляє помилки, пов'язані з відсутністю файлу або некоректним форматом даних.
    """
    salaries = [] # Список для зберігання зарплат

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    _, salary_str = line.split(',')
                    salary = int(salary_str)
                    salaries.append(salary)
                except ValueError:
                    print(f"Помилка даних: Пропускаємо рядок '{line}' через невірний формат зарплати.")
                except Exception as e:
                    print(f"Неочікувана помилка при обробці рядка '{line}': {e}")
            
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено. Повертаємо (0, 0).")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return (0, 0)

    # Обчислення результатів
    total_sum = sum(salaries)
    count = len(salaries)
    average_salary = total_sum / count if count > 0 else 0

    return (total_sum, average_salary)

if __name__ == '__main__':
    # Створюємо тестовий файл
    test_data = "Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\nInvalid line\n"
    test_file_path = "salary_file.txt"
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write(test_data)

    print("--- Аналіз зарплат ---")
    total, average = total_salary(test_file_path)
    print(f"Загальна сума: {total}, Середня зарплата: {average}") 

    # Перевірка відсутнього файлу
    total_missing, average_missing = total_salary("missing_file.txt")
    print(f"Загальна сума (немає файлу): {total_missing}, Середня (немає файлу): {average_missing}")

    try:
        os.remove(test_file_path)
    except Exception:
        pass
