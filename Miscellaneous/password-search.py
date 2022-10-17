import random


def search_password():
    password = ''
    password_search = input("Write your password: ")
    while password != password_search: 
        password = ''
        for select in range(len(password_search)):
            password += random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm'))
        print(password)
    return f'Your password {password}'
print(search_password())
