extenso = ('Zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while not (0 <= num <= 20):
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print