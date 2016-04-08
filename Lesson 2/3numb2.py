a = int(input('NUMBER 1 HERE '))
b = int(input('NUMBER 2 HERE '))
c = int(input('NUMBER 3 HERE '))
if a == b == c:
    print ('3')
elif (a == b != c) or (a != b == c) or (a == c != b):
    print ('2')
else:
    print ('0')
