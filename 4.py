years = int(input("Введите год : "))

def is_year_leap(year):
    if (year 
    % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year, "високосный год")
    else:
        print(year, "Год не високосный")

is_year_leap(years)

