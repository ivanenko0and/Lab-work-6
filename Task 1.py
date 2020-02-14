
"""
Програма визначає наступний та попередній дні від заданої дати D, M, Y.
"""

answer, m31, m30 = '1', [1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11]
days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)

while answer == '1':

    d, m, y, leap = 0, 0, 0, 0

    while True:
        try:
            y = int(input('Enter year:'))
            if y in years:
                break
            else:
                print("Enter year between 1901 and 2019!")
        except ValueError:
            print("Enter numbers only!")
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        leap = 1

    while True:
        try:
            m = int(input('Enter month:'))
            if m in months:
                break
            else:
                print("Enter proper month!")
        except ValueError:
            print("Enter numbers only!")

    while True:
        try:
            d = int(input('Enter day:'))
            if (m in m31 and d in days) or (m in m30 and d in range(1, 31)) or \
                    (m == 2 and d in range(1, 29) and leap == 0) or (m == 2 and d in range(1, 30) and leap == 1):
                break
            else:
                print("Enter proper day!")
        except ValueError:
            print("Enter numbers only!")

    nd, nm, ny = d, m, y
    if (m in m31 and d == 31) or (m in m30 and d == 30) or (m == 2 and d == 28 and leap == 0) \
            or (m == 2 and d == 29 and leap == 1):
        nd = 1
        if m == 12:
            nm = 1
            ny = y + 1
        else:
            nm = m + 1
    else:
        nd = d + 1

    if nd // 10 == 0:
        nd = str(f'0{nd}')
    if nm // 10 == 0:
        nm = str(f'0{nm}')
    print(f"Tomorrow date is: {nd}.{nm}.{ny}")

    nd, nm = int(), int()
    if d == 1:
        if m - 1 in m31:
            nd = 31
        elif m - 1 in m30:
            nd = 30
        elif m - 1 == 2 and leap == 0:
            nd = 28
        elif m - 1 == 2 and leap == 1:
            nd = 29
        nm = m - 1
        if m == 1:
            nd = 31
            nm = 12
            ny = y - 1
    else:
        nd = d - 1

    if nd // 10 == 0:
        nd = str(f'0{nd}')
    if nm // 10 == 0:
        nm = str(f'0{nm}')
    print(f"Yesterday date is: {nd}.{nm}.{ny}")

    answer = input("Want retry? Enter '1' to confirm:")

# Виконав Іваненко Андрій Вадимович
