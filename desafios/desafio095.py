jogadores = list()
jogador = dict()

while True:
    jogador.clear()  # Limpa o dicionário do jogador anterior
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

    gols = list()

    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na {c + 1}ª partida? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gol(s).')