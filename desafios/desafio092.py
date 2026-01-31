from datetime import date, datetime

data = date.today()

pessoa ={}

pessoa['nome'] = nome = str(input('Digite seu nome: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))
pessoa['idade'] = idade = date.today().year - ano_nasc
pessoa['ctps'] = carteira_trabalho = int(input('Carteira de Trabalho (0 não tem): '))
if carteira_trabalho != 0:
    pessoa['contratacao'] = ano_contrato = int(input('Digite o ano da sua contratação: '))
    pessoa['salario'] = salario = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = aposentadoria = (ano_contrato + 35) - ano_nasc

print('=-'*30)
print(pessoa)
print('=-'*30)

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')