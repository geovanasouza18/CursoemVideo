from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano_nascimento
if idade < 18:
    print('Calma, recruta! Você ainda não chegou na idade do alistamento. Aproveite a liberdade enquanto pode')
    tempo =
elif idade == 18:
    print('Atenção! É exatamente este o ano do seu alistamento. Hora de cumprir o dever!')
else:
    print('O prazo do alistamento expirou! Você está atrasado — trate de regularizar isso o quanto antes.')