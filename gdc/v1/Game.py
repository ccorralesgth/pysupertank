# state #1 
# generate basic concep ideas with bricks
# create main concept 

import pygame
from .Ui.Ui import Ui

class Game():
    def __init__(self):
        self.ui = Ui()        

    def run(self):        
        while self.ui.running:
            self.ui.runUILoop()
            
    
    def quit(self):
        pygame.quit()
        


