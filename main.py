a = float(input())
b = float(input())
c = float(input())

for x in range(1, 10):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + (d ** 0.5))/(2 * a)
        x2 = (-b - (d ** 0.5))/(2 * a)
        print(x1, x2)
        break
    elif d == 0:
        x = -b / (2 * a)
        print(x)
        break
    else:
        print("Корней нет")
        break