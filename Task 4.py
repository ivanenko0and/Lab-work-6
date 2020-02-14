
"""
Програма визначає колір світлофора, який горить для водіїв від початку години у заданий час у хвилинах T.
"""

answer = '1'
while answer == '1':

    while True:
        try:
            t = float(input('Enter time(in minutes):'))
            if 0 < t < 60:
                break
            else:
                print("Enter proper time!")
        except ValueError:
            print("Enter numbers only!")

    if 0 < t % 6 < 4:
        print("There's GREEN light is on.")
    elif t % 6 == 4:
        print("There's YELLOW light is on.")
    elif t % 6 == 5 or t % 6 == 0:
        print("There's RED light is on.")

    answer = input("Want retry? Enter '1' to confirm:")

# Виконав Іваненко Андрій Вадимович
