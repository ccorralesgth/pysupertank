#here will be the logic for the main concep idea
#concept game design idea

# lets merge a tank game with pacmac idea

import pygame
import os

class Ui():
    def __init__(self) -> None:
        pygame.init()               
        pygame.display.set_caption("SuperTank")
        #pygame.display.set_icon(pygame.image.load("assets/ui/icon.png"))        
        
        
        self.window = pygame.display.set_mode((int(500),int(500)))
        self.clock = pygame.time.Clock()       
        self.running = True
    
    def updateGameState(self):
        pass
        
    def renderUI(self):
        self.window.fill((255,255,255))
        pygame.display.update()
    
    def inputKeyboardMouse(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break                
    
    def quit(self):
        pygame.quit()
        
    def runUILoop(self):                
        self.inputKeyboardMouse()
        # self.updateGameState()
        self.renderUI()
        
           
