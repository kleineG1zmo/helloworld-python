a = int(input('CROSS 1 X'))
b = int(input('CROSS 1 Y'))
c = int(input('CROSS 2 X'))
d = int(input('CROSS 2 Y'))
if abs(c - a) == 2 and abs(d - b) == 1 or abs(d - b) == 2 and abs (c - a) == 1:
    print('YES')
else:
    print('NO')
