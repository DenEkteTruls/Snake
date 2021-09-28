import pygame
import random

class Food:

  def __init__(self, spots : list, food_size : int = 30) -> None:

    self.spots = spots
    self.food_size = food_size
    self.food = pygame.Rect(0, 0, 0, 0)
    self.update()


  def update(self) -> None:
    x = self.spots[random.randint(0, len(self.spots)-1)] + 10
    y = self.spots[random.randint(0, len(self.spots)-1)] + 10
    self.food = pygame.Rect(x, y, self.food_size, self.food_size)
  

  def render(self, screen) -> None:

    pygame.draw.rect(screen, (255, 0, 0), self.food)