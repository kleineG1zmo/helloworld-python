a = int(input('NUMBER 1 HERE '))
b = int(input('NUMBER 2 HERE '))
c = int(input('NUMBER 3 HERE '))
if a <= b:
    if b <= c:
        print (a)
    elif b >= c:
        if a >= c:
            print (c)
        else:
            print (a)
else:
    if a <= c:
        print (b)
    elif a >= c:
        if b >= c:
            print (c)
        else:
            print (b)
