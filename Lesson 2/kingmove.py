a = int(input('CROSS 1 X '))
b = int(input('CROSS 1 Y '))
c = int(input('CROSS 2 X '))
d = int(input('CROSS 2 Y '))
if ((a + 1) >= c >= (a - 1)) and ((b + 1) >= d >= (b - 1)):
    print ('YES')
else:
    print ('NO')
