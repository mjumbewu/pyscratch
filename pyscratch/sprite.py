import pygame
from math import sin, cos, radians, atan2, degrees
from random import randint

sprites = list()


class Sprite:
    def __init__(self):
        self.costumes = list()
        self.current_costume = 0
        self.surf = pygame.Surface((0, 0))
        self.disp_surf = pygame.Surface((0, 0))
        sprites.append(self)

        self.x = int(pygame.display.get_surface().get_rect().width / 2)
        self.y = int(pygame.display.get_surface().get_rect().height / 2)
        self._dir = 0
        self.rotation_style = "all-around"
        self.flip = False
        self.hidden = False

    def rotate(self, angle):
        if self.rotation_style == "all-around":
            self.disp_surf = pygame.transform.rotate(self.surf, angle)
        if self.rotation_style == "left-right":
            if abs(angle) <= 90 or abs(angle) >= 270:
                if self.flip:
                    self.disp_surf = self.surf
                    self.flip = False

            elif abs(angle) > 90 and abs(angle) < 270:
                if not self.flip:
                    self.disp_surf = pygame.transform.flip(self.surf, True, False)
                    self.flip = True

    def add_costume(self, costume_name, filepath):
        self.costumes.append([costume_name, pygame.image.load(filepath)])
        if len(self.costumes) == 1:
            self.current_costume = 0
            self.surf = self.costumes[0][1]
            self.disp_surf = self.surf

    def update_costume(self):
        self.surf = self.costumes[self.current_costume][1]
        self.disp_surf = self.surf
        self.rotate(-self._dir)

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, val):
        self._dir = val % 360
        self.rotate(self._dir)

    # SCRIPTS

    #   MOTION
    def move(self, value):
        self.x += cos(radians(self._dir)) * value
        self.y += sin(radians(self._dir)) * value

    def turn(self, value, dir=False):
        if dir:
            self._dir -= value
            self._dir = self._dir % 360
            self.rotate(-self._dir)

        else:
            self._dir += value
            self._dir = self._dir % 360
            self.rotate(-self._dir)

    def goto(self, location):
        if isinstance(location, tuple):
            self.x, self.y = location

        elif isinstance(location, Sprite):
            self.x, self.y = location.x, location.y

        elif location == "random-position":
            disp_rect = pygame.display.get_surface().get_rect()
            self.x, self.y = randint(0, disp_rect.width), randint(0, disp_rect.height)

        elif location == "mouse-position":
            mx, my = pygame.mouse.get_pos()
            self.x, self.y = mx, my

    def edge_bounce(self):
        disp_surf = pygame.display.get_surface().get_rect()
        if self.x + int(self.disp_surf.get_rect().width / 2) > disp_surf.width:
            self.x -= (
                self.x + int(self.disp_surf.get_rect().width / 2)
            ) - disp_surf.width
            self._dir = 180 - self._dir
            self.rotate(-self._dir)

        elif self.x - int(self.disp_surf.get_rect().width / 2) < 0:
            self.x += 0 - (self.x - int(self.disp_surf.get_rect().width / 2))
            self._dir = 180 - self._dir
            self.rotate(-self._dir)

        elif self.y + int(self.disp_surf.get_rect().height / 2) > disp_surf.height:
            self.y -= (
                self.y + int(self.disp_surf.get_rect().height / 2)
            ) - disp_surf.height
            self._dir = -self._dir
            self.rotate(-self._dir)

        elif self.y - int(self.disp_surf.get_rect().height / 2) < 0:
            self.y += 0 - (self.y - int(self.disp_surf.get_rect().height / 2))
            self._dir = -self._dir
            self.rotate(-self._dir)

    def point_to(self, location):
        if isinstance(location, tuple):
            self._dir = degrees(atan2(location[1] - self.y, location[0] - self.x)) % 360
            self.rotate(-self._dir)

        elif isinstance(location, Sprite):
            self._dir = degrees(atan2(location.y - self.y, location.x - self.x)) % 360
            self.rotate(-self._dir)

        elif location == "random-position":
            disp_rect = pygame.display.get_surface().get_rect()
            self._dir = (
                degrees(
                    atan2(
                        randint(0, disp_rect.height) - self.y,
                        randint(0, disp_rect.width) - self.x,
                    )
                )
                % 360
            )
            self.rotate(-self._dir)

        elif location == "mouse-position":
            mx, my = pygame.mouse.get_pos()
            self._dir = degrees(atan2(my - self.y, mx - self.x)) % 360
            self.rotate(-self._dir)

    #   LOOKS
    def show(self):
        self.hidden = False

    def hide(self):
        self.hidden = True

    def set_costume(self, costume_name):
        for i, costume in enumerate(self.costumes):
            if costume[0] == costume_name:
                self.current_costume = i
                self.update_costume()
                break

    def next_costume(self):
        self.current_costume += 1
        if self.current_costume > len(self.costumes) - 1:
            self.current_costume = 0
        self.update_costume()

    def costume(self, costume):
        if costume == "number":
            return self.current_costume
        elif costume == "name":
            return self.costumes[self.current_costume][0]
