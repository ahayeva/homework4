if __name__ == "__main__":
    day_number = int(input("Введіть номер дня тижня (1-7): "))

    if day_number == 1:
        print("понеділок")
    elif day_number == 2:
        print("вівторок")
    elif day_number == 3:
        print("середа")
    elif day_number == 4:
        print("четвер")
    elif day_number == 5:
        print("п'ятниця")
    elif day_number == 6:
        print("субота")
    elif day_number == 7:
        print("неділя")
    else:
        print("Невірний номер дня тижня")
        #EXERCISE 2
        month_number = int(input("Введіть номер місяця (1-12): "))

        if month_number == 1:
            print("січень")
        elif month_number == 2:
            print("лютий")
        elif month_number == 3:
            print("березень")
        elif month_number == 4:
            print("квітень")
        elif month_number == 5:
            print("травень")
        elif month_number == 6:
            print("червень")
        elif month_number == 7:
            print("липень")
        elif month_number == 8:
            print("серпень")
        elif month_number == 9:
            print("вересень")
        elif month_number == 10:
            print("жовтень")
        elif month_number == 11:
            print("листопад")
        elif month_number == 12:
            print("грудень")
        else:
            print("Невірний  місяць")
            #EXERCISE 3
            number = float(input("введіть число: "))

            if number > 0:
                print("number is positive")
            elif number < 0:
                print("number is negative")
            else:
                print("number is equal to zero")
                #EXERCISE 4
                number1 = float(input("Введіть перше число: "))
                number2 = float(input("Введіть друге число: "))

                if number1 == number2:
                    print(" рівнічисла")
                elif number1 < number2:
                    print(number1, number2)
                else:
                    print(number2, number1)
                    