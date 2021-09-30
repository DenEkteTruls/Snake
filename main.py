from classes.game import Game
from classes.tiles import Tiles
from classes.food import Food
from classes.snake import Snake

game = Game(500, 50)

tiles = Tiles(game.width, game.height, game.tile_size)
snake = Snake(game, tiles.spots)
food1 = Food(tiles.spots, game.tile_size)
food2 = Food(tiles.spots, game.tile_size)

game.add_objects([snake.head, food1.food, food2.food])

while game.running:
  # render tiles
  tiles.render(game.screen)

  # render food
  food1.render(game.screen)
  food2.render(game.screen)

  # render player (update)
  snake.render(game.screen)
  snake.check_if_eaten([food1, food2])
  snake.check_tail_collide()

  #event-handler
  game.event_handler()
  snake.event_handler(game.keys_pressed)

  #update
  game.clearScreen()
  game.fps_tick(60)

game.cleanUp()
