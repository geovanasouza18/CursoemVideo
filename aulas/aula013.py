for hello in range(10):
   print('Olá!')

#Contar de trás pra frente
for c in range(10 , 0, -1):
  print(c)
print('FIM')

#Pulando de 2 em 2
for a in range(0, 7, 2):
  print(a)

#Lendo um valor
num = int(input('Digite um valor: '))
for n in range(0, num+1):
    print(n)

#Usando o início, fim e passo
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
for d in range(a, b+1, c):
    print(d)

#Input dentro do for
for entrada in range(0, 4):
    numero = int(input('Digite um valor: '))

#Somatório de todos os valores
s = 0
for num in range(0, 5):
    numero = int(input('Digite um valor: '))
    s +=numero
print(f'O somatório de todos os valores é: {s}')

#Tabuada usando o for
for tab in range(1, 11):
    resultado = 7 * tab
    print(f'7 x {tab} = {resultado}')

#Contando Letras (mas SEM str!)
frase = "Eu sou um detetive do Python"
for i in range(len(frase)):
    print(frase[i])