a = int(input('NUMBER 1 X '))
b = int(input('NUMBER 1 Y '))
c = int(input('NUMBER 2 X '))
d = int(input('NUMBER 2 Y '))
if a%2 == 1:
    if b%2 == 1:
        N1 = int(1)
    else:
        N1 = int(0)
else:
    if b%2 == 0:
        N1 = int(1)
    else:
        N1 = int(0)
if c%2 == 1:
    if d%2 == 1:
        N2 = int(1)
    else:
        N2 = int(0)
else:
    if d%2 == 0:
        N2 = int(1)
    else:
        N2 = int(0)
if N1 == N2:
    print('YES!')
else:
    print('NOPE!')
