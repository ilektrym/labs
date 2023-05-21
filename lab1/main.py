print('Введите A B C для квадратного уравнения')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))
d = b**2 - 4 * a * c
if d > 0:
    x1 = ((-1)*b - d**0.5) / (2 * a)
    x2 = ((-1)*b + d**0.5) / (2 * a)
    print(x1,x2)
if d == 0:
    x = ((-1) * b) / (2 * a)
    print(x)
if d < 0:
    print('Корней НЕТ!!!')