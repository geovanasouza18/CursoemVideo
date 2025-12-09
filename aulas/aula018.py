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