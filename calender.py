a = int(input('PRINT YEAR HERE '))
if a % 4 == 0 and a % 400 == 0:
    print ('YES')
elif a % 4 == 0 and a % 100 == 0:
    print ('NO')
elif a % 4 == 0:
    print ('YES')
else:
    print ('NO')
