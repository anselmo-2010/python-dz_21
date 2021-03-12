def is_year_leap(year):
    if (year 
    % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year, "високосный год")
    else:
        print(year, "Год не високосный")

is_year_leap(2014)
is_year_leap(1984)
is_year_leap(1988)
is_year_leap(2019)
is_year_leap(2020)

