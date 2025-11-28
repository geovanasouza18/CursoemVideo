lanche = ('Burger', 'Juice', 'Pizza', 'Pudding', 'Chips') #Tuplas são imutáveis
print(lanche)
print(lanche[0:2])
print(lanche[1:])
print(lanche[-2])
print(lanche[0::2])
print(len(lanche))

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