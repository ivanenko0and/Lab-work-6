
"""
Програма переводить певну кількість грошей X із заданої валюти P в гривні.
"""

from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


print("(HINT: available currencies are: USD, EUR, CZK, PLN)")
answer = '1'
while answer == '1':

    while True:
        try:
            x = float(input('Enter amount of money:'))
            if x > 0:
                break
            else:
                print("Enter proper amount of money!")
        except ValueError:
            print("Enter numbers only!")
    while True:
        try:
            p = converter[input('Enter currency:')]
            break
        except KeyError:
            print("Enter proper currency!")

    if p == converter.USD:
        x *= 24.57
    elif p == converter.EUR:
        x *= 26.90
    elif p == converter.CZK:
        x *= 1.07
    elif p == converter.PLN:
        x *= 6.29
    print(f"The amount of money in UAH is: {x}.")

    answer = input("Want retry? Enter '1' to confirm:")

# Виконав Іваненко Андрій Вадимович
