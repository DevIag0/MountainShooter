from idlelib.query import Query

import pygame as py
from code.Menu import Menu
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.Level import Level

class Game:
    def __init__(self):
        py.init()  # inicializar o pygame
        self.window = py.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))  # criar a janela do jogo
        py.display.set_caption("MountainShooter")  # nome na janela

    def run(self):
        while True:
            menu = Menu(self.window)  # criar uma instância da classe Menu
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1],MENU_OPTION[2]]:
                print("Iniciar jogo 1P")
                level = Level(self.window, "Level 1", menu_return)
                level_return = level.run()


            elif menu_return == MENU_OPTION[3]:  # se a opção selecionada for "SCORE"
                print("Exibir pontuação")

            elif menu_return == MENU_OPTION[4]:  # se a opção selecionada for "EXIT"
                print("Sair do jogo")
                py.quit() # fechar o pygame
                quit()  # sair do programa
