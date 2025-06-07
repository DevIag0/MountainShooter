import pygame as py
from code.Menu import Menu  # importar a classe Menu do arquivo Menu.py

class Game:
    def __init__(self):
        py.init()  # inicializar o pygame
        self.window = py.display.set_mode((800, 600))  # criar a tela
        py.display.set_caption("MountainShooter")  # nome na janela

    def run(self):
        while True:
            menu = Menu(self.window)  # criar uma instância da classe Menu
            menu.run()
            #for event in py.event.get():
            #    if event.type == py.QUIT: #fechar a janela
            #        py.quit() #fechar o pygame
            #        exit()
            #atualizar a tela
            #py.display.update()

