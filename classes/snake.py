import pygame
import random

class Snake:

  def __init__(self, game : object, spots : list, snake_size : int = 40) -> None:

    self.game = game
    self.spots = spots
    self.snake_size = snake_size
    self.snake_margin = 5
    
    self.tails = []
    self.tails_to_add = []
    self.keys_pressed = {'w': False, 's': False, 'a': False, 'd': False}
    self.head = pygame.Rect(0, 0, 0, 0)
    self.color = (255, 140, 36)

    self.spawn_random()


  def spawn_random(self):

    x = self.spots[random.randint(0, len(self.spots)-1)] + self.snake_margin
    y = self.spots[random.randint(0, len(self.spots)-1)] + self.snake_margin
    self.head = pygame.Rect(x, y, self.snake_size, self.snake_size)

  
  def move(self, x : int, y : int) -> None:

    if round(self.head.x, 1) - self.snake_margin in self.spots and round(self.head.y, 1) - self.snake_margin in self.spots:
      if len(self.tails) > 0:
        self.tails = [pygame.Rect(self.head.x, self.head.y, self.snake_size, self.snake_size)]+self.tails[:-1]

    self.head.x += 5 * x
    self.head.y += 5 * y


  def check_tail_collide(self) -> None:

    if self.head.collidelistall(self.tails[1:]):
      self.game.running = False


  def add_tail(self, rect : object) -> None:

      tail = pygame.Rect(rect.x-self.snake_margin, rect.y-self.snake_margin, self.snake_size, self.snake_size)
      self.tails_to_add.append(tail)


  def add_queued_tail(self):

    for tail in self.tails_to_add:
      self.tails.append(tail)
    self.tails_to_add = []


  def event_handler(self, keys_pressed : list) -> None:

    if round(self.head.x, 1) - self.snake_margin in self.spots and round(self.head.y, 1) - self.snake_margin in self.spots:
      self.keys_pressed = keys_pressed
      if len(self.tails_to_add) > 0:
        if not self.head.colliderect(self.tails_to_add[0]):
          self.add_queued_tail()

    if self.keys_pressed['w'] : self.move(0, -1)
    elif self.keys_pressed['s'] : self.move(0, 1)
    elif self.keys_pressed['a'] : self.move(-1, 0)
    elif self.keys_pressed['d'] : self.move(1, 0)


  def check_if_eaten(self, food) -> None:

    if self.head.colliderect(food.food):
      self.add_tail(food.food)
      food.update()

  
  def render(self, screen : object) -> None:
    
    pygame.draw.rect(screen, self.color, self.head)

    for tail in self.tails:
      pygame.draw.rect(screen, self.color, tail)