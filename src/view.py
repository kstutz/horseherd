from world import *

import pygame

class View:

    tileWidth = 10
    tileHeight = 10

    def __init__(self):
        self._ground_surf = None
        self._animal_surf = None

    def render(self, world):
        windowWidth = world.width * self.tileWidth
        windowHeight = world.height * self.tileHeight

        self._ground_surf = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE)

        for row in range(world.height):
            for column in range(world.width):
                tile = world.getTile(row, column)
                color = tile.terrain

                if tile.has_horse:
                    color = (150,75,0)
                if tile.has_wolf:
                    color = (120, 120, 120)

                pygame.draw.rect(self._ground_surf, color,
                    [ column * self.tileWidth,
                      row * self.tileHeight,
                      self.tileWidth,
                      self.tileHeight])
