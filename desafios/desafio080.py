numeros = []

for c in range(5):
    numero = int(input("Digite um número: "))

    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            print(f"Valor {numero} inserido na posição {chave}")
            break
    else:
        numeros.append(numero)
        print(f"Valor {numero} inserido na posição {len(numeros)-1}")
print(f'Os valores digitados em ordem foram {numeros}')
