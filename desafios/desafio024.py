cidade = input("Digite o nome de uma cidade: ").strip()  # passo 1 e 2
if cidade[:5].upper() == "SANTO":                       # passo 3, 4 e 5
    print("A cidade começa com SANTO")
else:
    print("A cidade não começa com SANTO")
