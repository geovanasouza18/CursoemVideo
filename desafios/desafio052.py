primo = int(input('Digite um número: '))
total = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {primo} foi divisível {total} vezes.')
if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')