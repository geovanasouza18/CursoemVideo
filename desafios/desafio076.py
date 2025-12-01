print('-' * 35)
print('       LISTAGEM DE PREÇOS')
print('-' * 35)

listaProd = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

for i in range(0, len(listaProd), 2):
    produto = listaProd[i]
    preco = listaProd[i + 1]
    print(f'{produto:.<25} R${preco:>6.2f}')
