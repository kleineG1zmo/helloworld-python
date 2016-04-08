a = int(input('PIROZHOK COSTS, RUB '))
b = int(input('PIROZHOK COSTS, KOPEYKAS '))
n = int(input('WE NEED, PIROZHKOV '))
up = n * b // 100
if b >= 100:
    print('THIS IS IMPOSSIBLE, PLEASE PRINT NORMALLY! MAXIMAL NUMBER OF KOPEYKAS IS 99!')
elif up == True:
    print('IT`LL COST', (a * n) + up, 'RUB AND', (n * b) - up * 100, 'KOPEEK')
else:
    print('IT`LL COST', (a * n), 'RUB AND', (n * b), 'KOPEEK')
