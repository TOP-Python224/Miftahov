print('Введите координаты двух клеток шахматной доски: ')
a1 = ord(input('Введите значение первой координаты по горизонтали от "a" до "h": '))
a2 = int(input('Введите значение первой координаты по вертикали от 1 до 8: '))
b1 = ord(input('Введите значение второй координаты по горизонтали от "a" до "h": '))
b2 = int(input('Введите значение второй координаты по вертикали от 1 до 8: '))

a = a1 + a2
b = b1 + b2

if a % 2 == 0 and b % 2 ==0 or a % 2 != 0 and b % 2 != 0:
    print('Да')
else:
    print('Нет')