# state #1 
# generate basic concep ideas with bricks
# create main concept 

import pygame
from gdc.state1.Ui import Ui

class Game():
    def __init__(self):
        self.ui = Ui()        

    def run(self):        
        while self.ui.running:
            self.ui.runUILoop()
            #Each game step (input, update, and render) is run 60 times per second
            self.ui.clock.tick(60)   
    
    def quit(self):
        pygame.quit()
        


