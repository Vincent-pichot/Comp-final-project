import pygame
import sys
import math
import pygame
from events import EventHandler
from classes import *

UNSELECTED = "red"
SELECTED = "white"
BUTTONSTATES = {
    True:SELECTED,
    False:UNSELECTED
}

class UI:
    @staticmethod
    def init():
        UI.font = pygame.font.Font(None, 30)
        UI.sfont = pygame.font.Font(None, 20)
        UI.lfont = pygame.font.Font(None, 40)
        UI.xlfont = pygame.font.Font(None, 50)
        # UI.center = (app.screen.get_size()[0]//2, app.screen.get_size()[1]//2)
        # UI.half_width = app.screen.get_size()[0]//2
        # UI.half_height = app.screen.get_size()[1]//2

        UI.fonts = {
            'sm':UI.sfont,
            'm':UI.font,
            'l':UI.lfont,
            'xl':UI.xlfont
        }

class Menu:
    def __init__(self, app, bg="gray") -> None:
        print(app)
        self.app = app
        self.bg = bg
        UI.init()

        self.sliders = [
            Slider((1200,700), (300,40), 0.5, 1, 100),
        ]

    def run(self, planet_A):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        for slider in self.sliders:
            if slider.container_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    slider.grabbed = True
            if not mouse[0]:
                slider.grabbed = False
            if slider.button_rect.collidepoint(mouse_pos):  
                slider.hover()
            if slider.grabbed:
                slider.move_slider(mouse_pos)
                slider.hover()
            else:
                slider.hovered = False
            slider.render()
            slider.change_value(planet_A)
            slider.show_value()

class Label:
    def __init__(self, font: str, content: str, pos: tuple, value = "blue", selected: bool = False) -> None:
        self.font = font
        self.selected = selected
        self.content = content

        self.value = value

        self.text = UI.fonts[self.font].render(content, True, BUTTONSTATES[self.selected], None)
        self.text_rect = self.text.get_rect(center = pos)
    def render(self, app):
        app.screen.blit(self.text, self.text_rect)

        

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

        # label
        self.text = UI.fonts['m'].render(str(int(self.get_value())), True, "white", None)
        self.label_rect = self.text.get_rect(center = (self.pos[0], self.slider_top_pos - 15))
        
    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
    def hover(self):
        self.hovered = True
    def render(self):
        pygame.draw.rect(pygame.display.get_surface(), "darkgray", self.container_rect)
        pygame.draw.rect(pygame.display.get_surface(), BUTTONSTATES[self.hovered], self.button_rect)
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range)*(self.max-self.min)+self.min
    
    def change_value(self, planet_A):
        planet_A.set_masse((self.get_value()/100)*5.9722*math.pow(10,24))

    def show_value(self):
        self.text = UI.fonts['m'].render(str(int(self.get_value())), True, "white", None)
        pygame.display.get_surface().blit(self.text, self.label_rect)

class EventHandler:
    def __init__(self) -> None:
        EventHandler.events = pygame.event.get()
    def run():
        EventHandler.events = pygame.event.get()
    def clicked() -> bool:
        for e in EventHandler.events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False