teste = ['Geovana', 22]
galera = list()
galera.append(teste[:])
teste = ['Ana', 45]
galera.append(teste[:])
print(galera)

galera2 = [['Rebeca', 34], ['Hanna', 23], ['Samanta', 12], ['Carla', 19]]
print(galera2)
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos.')

galera3 = []
dado = []
totalmai = totalmen = 0
for c in range(0, 3):
    dado.append(str(input('Digite o nome da pessoa: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera3.append(dado[:])
    dado.clear()
for dados in galera3:
    if dados[1] >= 18:
        print(f'{dados[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{dados[0]} é menor de idade.')
        totalmen += 1
print(f'Temos {totalmai} pessoas maiores de idade e {totalmen} pessoas menores de idade.')