'''import math
catetoOposto = float(input("Digite o cateto oposto: "))
catetoadjacente = float(input("Digite o cateto adjacente: "))
calculo = math.hypot(catetoOposto **2 + catetoadjacente**2)
raiz = math.sqrt(calculo)
print("O valor da hipotenusa é {:.2f}: ".format(raiz))'''

#Corrigido
from math import hypot
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi = hypot(co, ca)
print("O valor da hipotenusa é: {:.2f} ".format(hi))
