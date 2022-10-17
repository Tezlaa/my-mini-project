from colorama import Back, Fore, Style, init

init()

print( Style.DIM)

print( Fore.MAGENTA)
print("Проверка Вашего числа")
number = 1
print( Fore.CYAN)

queation = input("Введите то ,на что Вы хотите проверить число (чётность; не чётность): ")
number_even = float(input("Введите число до какого нужно проверить: " ))
quetion_capitalize = str.capitalize(queation)


if quetion_capitalize == "Чётность":
    while number <= number_even:
        number += 1
        if (number % 2) !=0:
            continue;
        print("Число: " + str(number))
elif quetion_capitalize == "Не чётность":
    while number <= number_even:
        number += 1
        if (number % 2) == 0:
            continue;
        print("Число: " + str(number))
else :
    print("Проверьте написание параметров...")

input("Програма завершена..." )

