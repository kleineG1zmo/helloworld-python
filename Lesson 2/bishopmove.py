a = int(input('CROSS 1 X '))
b = int(input('CROSS 1 Y '))
c = int(input('CROSS 2 X '))
d = int(input('CROSS 2 Y '))
if (a - c) == (d - b) or (a - c) == -(d - b) or -(a - c) == (d - b):
    print ('YES')
else:
    print ('NO')
