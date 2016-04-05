a = int(input('LENGTH OF POOL '))
b = int(input('WIDTH OF POOL '))
c = int(input('METERS TO THE WIDE SIDE '))
d = int(input('METERS TO THE LONG SIDE '))
co = a - c
do = b - d
if c > a:
    print('IT IS IMPOSSIBLE!')  # cюда вставить функцию, которая обрывала бы график
if d > b:
    print('IT IS IMPOSSIBLE!')
array=[c,d,co,do];#об`явление массива
print(min(array));#вывод наименьшего.Ото й усе.
# if co > c:
#     if do > d:
#         if c > d:
#             print(d, 'METERS AT MINIMAL')
#         else:
#             print(c, 'METERS AT MINIMAL')
#     else:
#         if c > do:
#             print(do, 'METERS AT MINIMAL')
#         else:
#             print(c, 'METERS AT MINIMAL')
# else:
#     if do > d:
#         if co > d:
#             print(d, 'METERS AT MINIMAL')
#         else:
#             print(co, 'METERS AT MINIMAL')
#     else:
#         if co > do:
#             print(do, 'METERS AT MINIMAL')
#         else:
#             print(co, 'METERS AT MINIMAL')
