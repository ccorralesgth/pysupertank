#here will be the logic for the main concep idea
#concept game design idea

# lets merge a tank game with pacmac idea



import pygame
import os

class UserInterface():
    def __init__(self) -> None:
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        self.running = False
        self.window = pygame.display.set_modeset_mode((int(500),int(500)))
    
    def updateGameState(self):
        pass
    
    def runLoop(self):
        self.running = True
        while self.running:
            self.inputKeyboardMouse()
            self.updateGameState()
            self.renderUI()
            return
                
    def renderUI(self):
        self.window.fill((255,255,255))
        pass
    
    def inputKeyboardMouse(self):
        pass