import math
import random
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz do número {} é igual a {}".format(num,math.ceil(raiz)))
print("######### - Random - #############")
numChute = random.randint(1,20)
print(numChute)