peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Interessante… tão leve que até o vento te sequestra. Está abaixo do peso, meu caro.')
elif 18.5 <= imc < 25:
    print('Elementar! Peso ideal — equilíbrio digno de um verdadeiro Watson em forma.')
elif 25 <= imc < 30:
    print('Está no sobrepeso. Um empurrãozinho a mais e viramos caso de investigação nutricional.')
elif 30 <= imc < 40:
    print('Agora temos um caso sério: obesidade. Sugiro interrogarmos a geladeira imediatamente')
else:
    print('Obesidade mórbida. A situação é tão grave quanto confiar em Moriarty para guardar sua carteira.')