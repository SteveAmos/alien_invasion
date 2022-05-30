import pygame

class Ship:

    def __init__(self, ai_game):
        #initialize ship and set starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)