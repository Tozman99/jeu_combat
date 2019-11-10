import pygame


class Sol(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.rect = pygame.Rect(0, 470, 1100, 190)

	def afficher(self, surface):

		pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
