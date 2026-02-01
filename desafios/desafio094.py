media = total_mulheres = soma = maior_media = 0
dicionario = {}
pessoas = list()
while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dicionario['idade'] = int(input('Idade: '))
    pessoas.append(dicionario.copy())

    soma += dicionario['idade']
    if dicionario['sexo'] == 'F':
        total_mulheres += 1

    opcao = str(input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break


media = soma / len(pessoas)
print('='*45)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média do grupo é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram {total_mulheres} pessoas.')
print(f'- Lista de pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        maior_media +=1
    print(p)