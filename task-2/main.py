"""Calculates the sum of float numbers in the text
    """
from handlers import sum_profit
from generators import generator_numbers

# Приклад використання:
# text = "sdgsg sgswefgwef sgsdg ghgyjf s 20.00."
# text = "sdgji;aeg 20 sf00 30.0 20.0001 30.0 lkmlkm .3"

# pylint: disable=all
some_text = "Загальний дохід працівника складається з декількох частин: \
1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(some_text, generator_numbers)

print(f"Загальний дохід: {total_income}") # Загальний дохід: 1351.46
