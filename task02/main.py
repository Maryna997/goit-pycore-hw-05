import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для ідентифікації дійсних чисел у тексті:
    pattern = r"\b\d+.\d+\b" # Дійсні числа виглядають як одна або більше цифр, крапка, ще одна або більше цифр
    for match in re.finditer(pattern, text):
        yield float(match.group()) # Повертаємо дійсне число як результат

def sum_profit(text: str, func: Callable):
    total = sum(func(text))
    return total

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

