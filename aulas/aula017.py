lista = [1, 2, 3, 4]
lista.append(5)
print(lista)

#Usando o extend para adicionar mais de um valor
lista2 = [1, 2, 3, 4, 5]
lista2.extend([6, 7, 8])
print(lista2)

minha_lista = ["oi", "tudo", "bem?"]
print(minha_lista)
minha_lista.insert(1, "Python")
print(minha_lista)

lanche = ['hot dog', 'burger', 'juice', 'pizza', 'cookie']
print(lanche)
#Apaga pelo índice e retorna a lista
del lanche[1]
print(lanche)

#Apaga pelo índice e retorna o valor excluído, pode passar o índice, se não o fizer, ele apagará o último elemento
#OBS: ele só mostra o valor excluído quando criar uma nova variável
lanche.pop(0)
print(lanche)

#Diferente dos outros o remove apaga pelo valor
lanche.remove('pizza')
print(lanche)

#Excluí todos os elementos da lista
lista3 = ['Olá', 'Mundo']
print(lista3)
lista3.clear()
print(lista3)

#Criando uma lista usando o range
lista_range = list(range(1, 11))
print(lista_range)

#Usando o sort para ordenar os elementos
valores = [3, 7, 8, 4, 1, 9, 10]
print(valores)
valores.sort()
print(valores)

valores =list()
for cont in range(1, 6):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
list2.append(6)
print(list1)
print(list2)
