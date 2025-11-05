from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nascimento

print(idade)
if idade <= 9:
    print('As primeiras pistas da vida! Categoria MIRIM — futuro promissor, meu caro.')
elif idade <=14:
    print('Um jovem investigador em formação. Classificação: INFANTIL!')
elif idade <= 19:
    print('O raciocínio está afiado! Categoria JÚNIOR — quase pronto para casos reais.')
elif idade <= 20:
    print('Mente brilhante e experiente! Classificação: SÊNIOR — digno de acompanhar Holmes em investigações.')
else:
    print('Um verdadeiro mestre do jogo mental! Categoria MASTER — rival de Holmes em intelecto.')