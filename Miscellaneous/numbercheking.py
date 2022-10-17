from colorama import Back, Fore, Style, init

init()

print( Style.DIM)

print( Fore.MAGENTA)
print("Checking your number")
print( Fore.CYAN)


number = 1
queation = input("Enter what you want to check the number for (even; not even): ")
number_even = float(input("Enter the number up to which you want to check: "))
quetion_capitalize = str.capitalize(queation)


if quetion_capitalize == "Even":
    while number <= number_even:
        number += 1
        if (number % 2) !=0:
            continue;
        print("number: " + str(number))
elif quetion_capitalize == "Not even":
    while number <= number_even:
        number += 1
        if (number % 2) == 0:
            continue;
        print("number: " + str(number))
else :
    print("Check spelling of parameters...")

input("Program comleted..." )
