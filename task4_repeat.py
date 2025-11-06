s = float(input("Сума: "))
r = float(input("Відсоток: "))
m = int(input("Місяці: "))

p = s / m
x = r / 12 / 100
z = s

for i in range(1, m + 1):
    v = z * x
    all = p + v
    z -= p
    print(i, "міс:", "тіло=", p, "відс=", v, "всього=", all, "залишок=", z)
