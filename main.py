import pygame as py
#inicializar o pygame
init = py.init()

while True:
    #criar a tela
    screen = py.display.set_mode((800, 600))
    #criar o titulo
    py.display.set_caption("MountainShooter")
    #criar o loop do jogo
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    #atualizar a tela
    py.display.update()