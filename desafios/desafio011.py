larg = float(input("Largura da parede : "))
altu = float(input("Altura da parede: "))
area = larg * altu
print("Sua parede tem dimensão de {}x{} e sua área é de {}m².".format(larg, altu, area))
tinta = area / 2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))