nota1 = float(input('Digite sua primeira nota '))
nota2 = float(input('Digite sua segunda nota '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('🎉 Elementar! Você passou com distinção, meu caro estudante!')
elif 5.0 <= media <= 6.9: #simplificando
    print('🧹 Como Kiki em seu início: você precisa treinar mais para dominar o voo. RECUPERAÇÃO!')
else:
    print('💔 Erro no saque… REPROVADO. Mas corvos sempre levantam de novo!')