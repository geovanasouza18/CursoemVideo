n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3 #porque já foi mostrado o 1 e segundo termo
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
