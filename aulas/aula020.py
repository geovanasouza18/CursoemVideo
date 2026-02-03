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