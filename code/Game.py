import pygame as py
from code.Menu import Menu
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT

class Game:
    def __init__(self):
        py.init()  # inicializar o pygame
        self.window = py.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))  # criar a janela do jogo
        py.display.set_caption("MountainShooter")  # nome na janela

    def run(self):
        while True:
            menu = Menu(self.window)  # criar uma instância da classe Menu
            menu.run()
