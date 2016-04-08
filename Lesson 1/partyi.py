a = int(input('NUMBER OF STUDENTS IN 1ST CLASS '))
b = int(input('NUMBER OF STUDENTS IN 2ND CLASS '))
c = int(input('NUMBER OF STUDENTS IN 3RD CLASS '))
d = (a + b + c) // 2
e = (a + b + c) % 2
if e > 0:
    print('THE', d + 1, 'DECKS NEEDED')
else:
    print('THE', d, 'DECKS NEEDED')
