version = "0.0"
state = "pre-alpha"

import collections
import functools
import inspect
import logging
import time
import pygame

from pyscratch.sprite import Sprite, sprites
from pyscratch.keys import key_dictionary, key_pressed

log = logging.getLogger(__name__)


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

# DEFAULTS
project.size = (480, 360)
project.name = "Scratch Project"
project.icon = "pyscratch/assets/scratch-icon-bg16.png"

running = True
clock = pygame.time.Clock()
event_callbacks = collections.defaultdict(list)

# SCRIPT DEFAULTS


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

# SCRIPTS


def ensure_generatorfunction(func):
    if inspect.isgeneratorfunction(func):
        return func
    else:

        @functools.wraps(func)
        def generator_func(*a, **k):
            yield func(*a, **k)

        return generator_func


def mouse_down(button):
    m = pygame.mouse.get_pressed()

    if button == "left" and m[0]:
        return True
    elif button == "middle" and m[1]:
        return True
    elif button == "right" and m[2]:
        return True
    else:
        return False


def when_started(func):
    func = ensure_generatorfunction(func)
    gen = func()
    event_callbacks["start"].append(gen)


def run():
    global running, clock
    event_generator_queue = event_callbacks["start"]

    while running:
        # HANDLE EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # If there are no new events that have been triggered, or all triggered
        # events have finished running, then stop the run.
        log.debug(f"length of event generator queue is {len(event_generator_queue)}")
        if len(event_generator_queue) == 0:
            running = False

        for _ in range(len(event_generator_queue)):
            gen = event_generator_queue.pop()
            try:
                log.debug(f"running {gen}")
                next(gen)
            except StopIteration:
                log.debug(f"generator {gen} is done")
                pass
            else:
                log.debug(f"re-enqueing {gen}")
                event_generator_queue.append(gen)

        # RENDER AND UPDATE
        log.debug(f"rendering and updating")
        timer.secs = time.time() - timer.time_start
        mouse.x, mouse.y = pygame.mouse.get_pos()

        project.window.fill((255, 255, 255))

        for sprite in sprites:
            if not sprite.hidden:
                project.window.blit(
                    sprite.disp_surf,
                    (
                        sprite.x - int(sprite.disp_surf.get_rect().width / 2),
                        sprite.y - int(sprite.disp_surf.get_rect().height / 2),
                    ),
                )

        pygame.display.flip()
        clock.tick(project.fps)

    log.debug("quitting")
    pygame.quit()
