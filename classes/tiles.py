import pygame

class Tiles:

  def __init__(self, screen_width : int, screen_height : int, tile_size : int) -> None:

    self.tile_size = tile_size
    self.screen_width = screen_width
    self.screen_height = screen_height

    self.tiles = []
    self.spots = [e for e in range(screen_width) if e%self.tile_size == 0 and screen_width - e >= self.tile_size]

    self.renderTiles()


  def renderTiles(self) -> None:

    for x in range(len(self.spots)):
      for y in range(len(self.spots)):
        if y%2 == 0:
          if x%2 == 0:
            tile = {'rect': pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size), 'color': (153,226,101)}
          else:
            tile = {'rect': pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size), 'color': (46,178,255)}
          self.tiles.append(tile)
        else:
          if x%2 == 1:
            tile = {'rect': pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size), 'color': (153,226,101)}
          else:
            tile = {'rect': pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size), 'color': (46,178,255)}
          self.tiles.append(tile)

  
  def render(self, screen : object) -> None:

    for tile in self.tiles:
      pygame.draw.rect(screen, tile['color'], tile['rect'])
