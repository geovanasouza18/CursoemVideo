celsus = float(input("Informe a temperatura em °C: "))
conversorCel = (celsus * 1.8) + 32
print("Portanto, {}°C é igual a {}°F.".format(celsus, conversorCel))

fahrenheit = float(input("Informe a temperatura em °F: "))
conversorFah = (fahrenheit - 32) * 5/9
print("Portanto, {}°F é igual a {}°C.".format(fahrenheit, conversorFah))
