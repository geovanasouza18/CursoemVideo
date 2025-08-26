preco = float(input("Qual o preço do produto? R$"))
novo = preco - (preco * 14 / 100)
print("O valor do produto com desconto de 20% é R${:.2f}".format(novo))