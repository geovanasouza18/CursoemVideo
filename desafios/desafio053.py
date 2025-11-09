frase = input('Digite uma frase: ').strip()
frase = frase.replace(' ', '')
frase = frase.lower()

inverso = ''
for i in range(len(frase) - 1, -1, -1):
    inverso += frase[i]

if inverso == frase:
    print('Essa frase é um Palíndromo')
else:
    print('Essa frase não é um Palíndromo')
