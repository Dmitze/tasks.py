import datetime
import random
import re

# --- Завдання 1: Дні до/після дати ---
def get_days_from_today(date_str):
    try:
        d = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.datetime.today().date()
        diff = today - d
        return diff.days
    except ValueError:
        return "Помилка: треба 'РРРР-ММ-ДД'."
    except Exception as e:
        return f"Помилка: {e}"

# --- Завдання 2: Лотерейні числа ---
def get_numbers_ticket(min_num, max_num, quantity):
    
    if min_num < 1 or max_num > 1000 or quantity <= 0: return []
    if quantity > (max_num - min_num + 1): return []

    try:
        nums = random.sample(range(min_num, max_num + 1), quantity)
        return sorted(nums)
    except:
        return []


# --- Завдання 3: Чистий телефон ---
def normalize_phone(phone_number):
    
    digits = re.sub(r'\D', '', phone_number) 
    
    if digits.startswith('380'):
        return '+' + digits
    
    if digits.startswith('0') and len(digits) == 10:
        return '+38' + digits

    if len(digits) == 10:
        return '+380' + digits

    if digits.startswith('38') and len(digits) == 12:
        return '+' + digits
        
    if len(digits) >= 9:
        return '+' + digits
        
    return digits


# --- Завдання 4: Привітання на тижні ---
def get_upcoming_birthdays(users):
    
    today = datetime.datetime.today().date()
    birthdays = []
    limit = today + datetime.timedelta(days=7)

    for user in users:
        try:
            bday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            bday_this_year = bday.replace(year=today.year)

            if bday_this_year < today:
                bday_this_year = bday.replace(year=today.year + 1)

            if today <= bday_this_year < limit:
                c_date = bday_this_year
                day_of_week = bday_this_year.weekday()

                if day_of_week == 5: # Сб
                    c_date += datetime.timedelta(days=2)
                elif day_of_week == 6: # Нд
                    c_date += datetime.timedelta(days=1)
                
                birthdays.append({
                    "name": user["name"],
                    "congratulation_date": c_date.strftime("%Y.%m.%d")
                })

        except ValueError:
            continue

    return birthdays

if __name__ == '__main__':
    print("="*60)
    print("--- ЗАВДАННЯ 1: Дні до/після дати ---")
    days_in_future = get_days_from_today("2026-05-15")
    print(f"Дні від 2026-05-15 до сьогодні: {days_in_future}")

    days_in_past = get_days_from_today("2024-01-01")
    print(f"Дні від 2024-01-01 до сьогодні: {days_in_past}")


    print("\n"+"="*60)
    print("--- ЗАВДАННЯ 2: Лотерейні числа ---")
    
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(f"Лотерея (1-49, 6 шт.): {lottery_numbers}")
    
    invalid_numbers = get_numbers_ticket(1, 1500, 5) 
    print(f"Невалідний діапазон: {invalid_numbers}")
    
    invalid_quantity = get_numbers_ticket(1, 5, 10) 
    print(f"Забагато чисел: {invalid_quantity}")


    print("\n"+"="*60)
    print("--- ЗАВДАННЯ 3: Чистий телефон ---")

    raw_numbers = [
        "067\t123 4567", "+380 44 123 4567", "380501234567", "     0503451234",
        "38050-111-22-22", "+1 (202) 555 0100", "+38 050 111 22 33", "0998887766" 
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Чисті номери:")
    print(sanitized_numbers)


    print("\n"+"="*60)
    print("--- ЗАВДАННЯ 4: Привітання на тижні ---")

    users_data = [
        {"name": "Олена", "birthday": "1990.10.15"}, 
        {"name": "Іван", "birthday": "1988.10.18"},  
        {"name": "Марія", "birthday": "1995.10.19"}, 
        {"name": "Петро", "birthday": "1980.10.20"}, 
    ]

    upcoming_birthdays = get_upcoming_birthdays(users_data)
    print("Кого вітати:")
    
    sorted_birthdays = sorted(upcoming_birthdays, key=lambda x: x['congratulation_date'])
    for entry in sorted_birthdays:
        print(f" - {entry['name']}: {entry['congratulation_date']}")

    print("="*60)
