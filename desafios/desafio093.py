jogador = dict()
gols = list()
jogador['nome'] = nome = str(input('Digite o nome do jogador: '))
jogador['gols'] = partidas = int(input(f'Quantas partidas {nome} jogou: '))
for c in range(1, partidas + 1):
    qtde_gols = int(input(f'Quantos gols na {c} partida : '))
    gols.append(qtde_gols)
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(jogador['gols'])

print('=-'*30)
print(jogador)
print('=-'*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for i, g in enumerate(jogador['gols'], 1):
    print(f'   => Na partida {i}, fez {g} gols.')