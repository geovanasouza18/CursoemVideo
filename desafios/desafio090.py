#Desafio 90
alunos = {}
alunos['Nome'] = str(input('Digite o nome do aluno: '))
alunos['Media'] = float(input('Digite a média do aluno: '))
if alunos['Media'] >= 7:
    alunos['Situacao'] = 'Aprovado'
else:
    alunos['Situacao'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')