c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')

n = 0
contador = 0
while n != 3:
    n = int(input('Digite um número: '))
    if n != 3:  # só conta se não for o número que encerra
        contador += 1
print(f'Você digitou {contador} números antes do fim!')

palavra_secreta = 'Sherlock'

#Usando while True
while True:
    palavra = input('Digite uma palavra: ')
    if palavra == palavra_secreta:
        break