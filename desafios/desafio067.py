print('-' * 30)
print('TABUADA — DESAFIO 67')
print('-' * 30)
while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 30)

print('PROGRAMA ENCERRADO. VOLTE SEMPRE!')
