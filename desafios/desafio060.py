num = int(input('Digite um número para calcular o fatorial: '))
c = num
f = 1
while c > 0:
    print(f'{c}', end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)
