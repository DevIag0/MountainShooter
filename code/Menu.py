import pygame as py
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WINDOW_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = py.image.load("./asset/MenuBg.png") #carregar a imagem de fundo
        self.rect = self.surf.get_rect(left=0, top=0) # definir a posição da imagem de fundo

    def run(self, ):
        py.mixer.music.load("./asset/Menu.mp3")  # carregar a música de fundo
        py.mixer_music.play(-1) # tocar a música de fundo em loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect) # desenhar a imagem de fundo
            self.menu_text(text_size=50, text="Mountain", text_color=(COLOR_ORANGE),
                           text_center_pos=((WINDOW_WIDTH - 20), 70))  # desenhar o texto "Mountain"
            self.menu_text(text_size=50, text="Shooter", text_color=(COLOR_ORANGE),
                           text_center_pos=(WINDOW_WIDTH - 20, 120))  # desenhar o texto "Mountain"

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=(COLOR_WHITE),
                               text_center_pos=(WINDOW_WIDTH, 180 + 30 * i))

            py.display.flip()  # atualizar a tela
            #checar eventos
            for event in py.event.get():
                if event.type == py.QUIT: #fechar a janela
                    py.quit() #fechar o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = py.font.SysFont("Lucida Sans Typewriter", size=text_size)  # carregar a fonte
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # definir a posição do texto
        self.window.blit(source=text_surf, dest=text_rect)  # desenhar o texto na tela
