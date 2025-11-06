from shop import *

while True:
    д = input("Дія (додати/показати/знайти/вихід): ")
    if д == "додати":
        n = input("Назва: ")
        c = float(input("Ціна: "))
        k = int(input("Кількість: "))
        add(n, c, k)
    elif д == "показати":
        show()
    elif д == "знайти":
        n = input("Назва: ")
        t = find(n)
        if t:
            print(t.n, t.c, "грн", t.k, "шт")
        else:
            print("Нема")
    elif д == "вихід":
        break
