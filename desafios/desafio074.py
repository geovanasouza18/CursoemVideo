import random
numerosAleatorias = tuple(random.randint(0, 10) for _ in range(5))
print(f'Os valores sorteados foram {numerosAleatorias}')
maior = max(numerosAleatorias)
menor = min(numerosAleatorias)
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
