import pygame

class Game:
  
  def __init__(self, width : int, tile_size : int = 50) -> None:

    self.score = 0
    self.width = width
    self.height = width
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.keys_pressed = {'w': False, 's': False, 'a': False, 'd': False}
    self.tile_size = tile_size
    self.game_objects = []
    self.running = True


  def activate_key(self, key : chr) -> None:
  
    self.keys_pressed = {'w': False, 's': False, 'a': False, 'd': False}
    self.keys_pressed[key] = True


  def event_handler(self) -> None:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          self.activate_key('w')
        elif event.key == pygame.K_s:
          self.activate_key('s')
        elif event.key == pygame.K_a:
          self.activate_key('a')
        elif event.key == pygame.K_d:
          self.activate_key('d')
        elif event.key == pygame.K_ESCAPE:
          self.running = False
    for object_ in self.game_objects:
      if object_.x < 0 or object_.x > self.width - self.tile_size/2:
        self.running = False
      if object_.y < 0 or object_.y > self.height - self.tile_size/2:
        self.running = False


  def add_objects(self, objects : list) -> None:

    for object_ in objects:
      self.game_objects.append(object_)


  def fps_tick(self, fps : int) -> None:

    self.clock.tick(fps)


  def clearScreen(self) -> None:

    pygame.display.flip()

  
  def cleanUp(self) -> None:

    print("Snake game closing ...")
    print(f"You got {self.score} points!")
