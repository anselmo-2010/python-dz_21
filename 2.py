def fizz_buzz():
    num = int(input("Введите число :"))
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num  % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

fizz_buzz()
