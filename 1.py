arg = int(input("Введите количество звездочек :"))

def show_stars(rows):
    stars = " "
    for i in range(rows):
        stars +="*"
        print(stars)

show_stars(arg)

# разбор дз

def show_stars(rows):
    for in in range(rows):
        print("*" * (i + 1))
        
show_stars(5)
