somaidade = 0
mediaidade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalmulher = 0
for pessoa in range (1,5):
    print(f'----- {pessoa}ª pessoa -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo == 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if  sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}.')
print (f'Ao total {totalmulher} mulheres com menos de 20 anos.')
