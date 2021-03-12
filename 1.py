stars = int(input("Введите количество звездочек :"))

def show_stars(rows):
    stars = " "
    for i in range(rows):
        stars +="*"
        print(stars)

show_stars(stars)
