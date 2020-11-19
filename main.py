def intro():
    print('Hello! My name is Shalopay!')
    print('I was created in 2020.')


def enter_name():
    name = input('Please remind me your name.\n')
    print(f'What a great name you have, {name}!')


def calc_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem_3 = int(input())
    rem_5 = int(input())
    rem_7 = int(input())
    age = (rem_3 * 70 + rem_5 * 21 + rem_7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def calc_num():
    count = int(input('Now I will prove to you that I can count to any number you want.\n'))
    for i in range(count + 1):
        print(i, '!')
        i += 1


def test():
    print("Let's test your programming knowledge.")
    answer = 0
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    while answer != 2:
        answer = int(input())
        print('Please, try again.')
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


intro()
enter_name()
calc_age()
calc_num()
test()
end()
