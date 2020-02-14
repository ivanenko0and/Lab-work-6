
"""
Програма визначає пору року за заданим місяцем S.
"""

from enum import Enum


class month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


answer = '1'
while answer == '1':

    while True:
        try:
            s = month[input('Enter month:')]
            break
        except KeyError:
            print("Enter proper month!")

    if s is month.December or s is month.January or s is month.February:
        print("This month belongs to Winter.")
    elif s is month.March or s is month.April or s is month.May:
        print("This month belongs to Spring.")
    elif s is month.June or s is month.July or s is month.August:
        print("This month belongs to Summer.")
    elif s is month.September or s is month.October or s is month.November:
        print("This month belongs to Autumn.")

    answer = input("Want retry? Enter '1' to confirm:")

# Виконав Іваненко Андрій Вадимович
