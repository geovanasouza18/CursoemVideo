name = str(input("Digite um nome: "))
if name == 'Geovana':
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Esse nome é bem popular no Brasil!')
elif name in 'Ana Katy Jéssica Paula Rebeca':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum!')
print(f'Tenha um bom dia, {name}!')