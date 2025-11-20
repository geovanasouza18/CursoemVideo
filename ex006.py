print('Número de 1 a 5 e multiplicando por 2 usando o for')
for i in range(1,6):
    print(i * 2)

print('Número de 1 a 5 e multiplicando por 2 usando o while')
contador = 0
while contador <= 5:
    print(contador * 2)
    contador += 1

print('Usando o break')

contador2 = 0
while True:
    print(contador2 * 2)
    contador2 += 1
    if contador2 == 20:
        break

#Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um número indeterminado de pessoas enquanto quiser e os mostre na tela ao finalizar.
listas1 = []
nome = ''
while nome != '0':
    nome = input('Digite um nome ou 0 para sair: ')
    if nome != '0':
        listas1.append(nome)
print(listas1)