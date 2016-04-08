n = int(input('HOW MANY MINUTES CAME? '))
h = n // 60
m = n % 60
d = n // 1440
if d >= 1:
    print('IT`S', h - (24 * d), m)
else:
    print('IT`S', h, m)
