import pygame
import random

class Food:

  def __init__(self, spots : list, tile_size : int = 50) -> None:

    self.spots = spots
    self.tile_size = tile_size
    self.food_size = tile_size*0.6
    self.food = pygame.Rect(0, 0, 0, 0)
    self.update()


  def update(self) -> None:
    x = self.spots[random.randint(0, len(self.spots)-1)] + self.tile_size*0.2
    y = self.spots[random.randint(0, len(self.spots)-1)] + self.tile_size*0.2
    self.food = pygame.Rect(x, y, self.food_size, self.food_size)
  

  def render(self, screen) -> None:

    pygame.draw.rect(screen, (255, 0, 0), self.food, 0, border_radius=4)