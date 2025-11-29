lanche = ('Burger', 'Juice', 'Pizza', 'Pudding', 'Chips') #Tuplas são imutáveis
print(lanche)
print(lanche[0:2])
print(lanche[1:])
print(lanche[-2])
print(lanche[0::2])
print(len(lanche))
index1 = lanche.index("Pizza")
print(f"Índice da Pizza: {index1}")

#Mostrando a tupla em ordem
print('Mostrando a Tupla em ordem')
print(sorted(lanche))

print('=' * 30)

#Forma 1
for i in lanche:
    print(i)

print('=' * 30)

#Forma 2
for pos, i in enumerate (lanche):
    print(i , pos)

print('=' * 30)

#Forma 3
for cont in range(0, len(lanche)):
    print(lanche[cont], cont)

#Juntando Tuplas
print('=' * 30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(5))

pessoa = ('João', 21, '2003', 'Brasil')
del (pessoa)
print(pessoa)