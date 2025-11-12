sexo = str(input('Digite seu sexo: ')).strip().upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo registrado com sucesso!')