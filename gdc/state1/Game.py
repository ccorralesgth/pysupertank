# state #1 
# generate basic concep ideas with bricks
# create main concept 

import pygame
from Ui import *

class Game():
    def __init__(self):
        self.userInterface = UserInterface()        

    def run(self):        
        while self.userInterface.running:
            self.userInterface.processInput()            
            self.userInterface.update()
            self.userInterface.render()
            #Each game step (input, update, and render) is run 60 times per second
            self.userInterface.clock.tick(60)
    
    def quit(self):
        pygame.quit()
        


