import pygame


class Joueur(pygame.sprite.Sprite):

	def __init__(self, x, y, taille):
		super().__init__()
		self.x = x
		self.y = y
		self.taille = taille
		self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
		self.saut_montee = 0
		self.saut_descente = 5
		self.saut = 0
		self.a_sauter = False
		self.nombre_de_saut = 0

	def sauter(self):

		if self.a_sauter is True:

			if self.saut_montee >= 10:
				self.saut_descente -= 1
				self.saut = self.saut_descente
			else:
				self.saut_montee += 1
				self.saut = self.saut_montee

			if self.saut_descente < 0:
				self.saut_descente = 0
				self.saut_montee = 5
				self.a_sauter = False

		self.rect.y = self.rect.y - (10 * (self.saut/2))

	def mouvement(self, vitesse):
		self.rect.x += vitesse



	def afficher(self, surface):

		pygame.draw.rect(surface, (0, 255, 255), self.rect)
