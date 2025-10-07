"""print("\033[0;41mTeste")
print("\033[1;45mOlá Mundo!")"""
a = 2
b = 3
print("Os valores são \033[1;32m{}\033[m e \033[1;36m{}\033[m".format(a, b))

nome = "Geovana"
print("Olá! Muito prazer em te conhecer, {}{}{}".format("\033[4;34m", nome, "\033[m")) # Outra forma de usar os códigos

# Outra forma de usar os códigos
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m', }
name = "Ana"
print("Olá! Muito prazer em te conhecer, {}{}{}".format(cores["amarelo"], name, cores['limpa']))

