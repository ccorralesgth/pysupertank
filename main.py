from gdc.state1.Game import Game
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

game = Game()
game.run()
game.quit()
    