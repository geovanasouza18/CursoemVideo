import pygame

pygame.init()
pygame.mixer.music.load(r"C:\Users\User\PycharmProjects\PythonProject\arquivos\belong together.mp3")
pygame.mixer.music.play(loops=-1, start=4.6)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)