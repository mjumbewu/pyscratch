version = "0.0"
state = "pre-alpha"

import time
import pygame

from pyscratch.sprite import Sprite, sprites
from pyscratch.keys import key_dictionary, key_pressed

class Project:
    def __init__(self):
        self._name = None
        self._size = None
        self._icon = None

        self.fps = 60

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val
        pygame.display.set_caption(self._name)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val
        self.window = pygame.display.set_mode(self._size)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, val):
        self._icon = val
        pygame.display.set_icon(pygame.image.load(self._icon))

project = Project()

#DEFAULTS
project.size = (480, 360)
project.name = "Scratch Project"
project.icon = "pyscratch/assets/scratch-icon-bg16.png"

running = True
clock = pygame.time.Clock()

#SCRIPT DEFAULTS

class Timer:
    def __init__(self):
        self.time_start = time.time()
        self.secs = 0

    def reset(self):
        self.time_start = time.time()

timer = Timer()

class Mouse:
    def __init__(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]

mouse = Mouse()

#SCRIPTS

def mouse_down(button):
    m = pygame.mouse.get_pressed()

    if button == "left" and m[0]: return True
    elif button == "middle" and m[1]: return True
    elif button == "right" and m[2]: return True
    else: return False


def run(main_func):
    global running, clock

    while running:
        #HANDLE EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #RENDER AND UPDATE
        timer.secs= time.time() - timer.time_start
        mouse.x, mouse.y = pygame.mouse.get_pos()

        main_func()

        project.window.fill((255, 255, 255))

        for sprite in sprites:
            if not sprite.hidden:
                project.window.blit(sprite.disp_surf, (sprite.x - int(sprite.disp_surf.get_rect().width / 2),
                                                       sprite.y - int(sprite.disp_surf.get_rect().height / 2)))

        pygame.display.flip()
        clock.tick(project.fps)

    pygame.quit()
