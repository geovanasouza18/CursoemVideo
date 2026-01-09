filmes = {'titulo': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}

for K, V in filmes.items():
    print(f'{K} - {V}')

filme = [
    {'titulo': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'},
    {'Titulo': 'The Avengers', 'Ano': 2012, 'Diretor': 'Joss Whedon'},
    {'Titulo': 'Matrix', 'Ano': 1999, 'Diretor': 'Wachowski'},
]
for ordem in filme:
    print(ordem)

pessoa = {'Nome': 'Geovana', 'Idade': 22}
print(pessoa['Nome'], pessoa['Idade'])
pessoa['Sexo'] = 'Feminino'
print(pessoa.keys())
print(pessoa.values())
for k, v in pessoa.items():
    print(f'{k} - {v}')