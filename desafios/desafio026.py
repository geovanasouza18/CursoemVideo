frase = input("Digite uma frase: ").upper().strip()
posicao = frase.find("A")
if posicao != -1:
    print(f"A primeira letra 'A' aparece na posição {posicao}")
else:
    print("Não existe a letra 'A' na frase")
