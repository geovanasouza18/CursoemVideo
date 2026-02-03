#Sem usar a função
print('-='*20)
print('Curso em Vídeo')
print('-='*20)
print('-='*20)
print('Aprendendo Função em Python')
print('-='*20)
print('-='*20)
print('Com o Prof. Gustavo Guanabara')
print('-='*20)

#Com a função
def criar_linha():
    print('-='*20)


print('Curso em Vídeo - usando função')
criar_linha()
print('Aprendendo Função em Python')
criar_linha()
print('Com o Prof. Gustavo Guanabara')
criar_linha()

#Usando o parâmetro
def titulo(txt):
    print('='*30)
    print(txt)


titulo('Python é muito bom!')
titulo('Usando parâmetro')
titulo('Curso em Vídeo')

#Prática
def soma(a, b):
    print(f'A soma de {a} e {b}.')
    soma = a + b
    print(soma)

soma(6, 5)
soma(8, 4)
soma(6, 2)

criar_linha()
#Usando o * para desempacotar um parâmetro
def contador (*num):
    for n in num:
        print(n)


contador(1, 2, 3)
criar_linha()
contador(4, 5)
criar_linha()
contador(8, 0, 4, 1, 6, 12)
criar_linha()

def dobro(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [4, 5, 6, 8, 10]
print(valores)
dobro(valores)
print(valores)