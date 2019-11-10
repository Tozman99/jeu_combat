import pygame
import sys
from joueur import Joueur
from sol import Sol


class Jeu:

	def __init__(self):

		self.ecran = pygame.display.set_mode((1100, 600))
		pygame.display.set_caption('Jeu Combat')
		self.jeu_encours = True
		self.joueur_x, self.joueur_y = 700, 200
		self.joueur_vitesse_x = 0
		self.joueur_taille = [32, 64]
		self.joueur = Joueur(self.joueur_x, self.joueur_y, self.joueur_taille)
		self.sol = Sol()
		self.gravite = (0, 10)
		self.resistance = (0, 0)
		self.clock = pygame.time.Clock()
		self.fps = 30
		self.rect = pygame.Rect(0, 0, 1100, 600)
		self.collision_sol = False

	def gravite_jeu(self, vecteur1, vecteur2):

		self.joueur.rect.y += vecteur1[1] + vecteur2[1]

	def boucle_principale(self):

		while self.jeu_encours:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.joueur_vitesse_x = 10

					if event.key == pygame.K_LEFT:
						self.joueur_vitesse_x = -10

					if event.key == pygame.K_UP:
						self.joueur.a_sauter = True
						self.joueur.nombre_de_saut += 1

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						self.joueur_vitesse_x = 0

					if event.key == pygame.K_LEFT:
						self.joueur_vitesse_x = 0

			if self.sol.rect.colliderect(self.joueur.rect):

				self.resistance = (0, -10)
				self.collision_sol = True
				self.joueur.nombre_de_saut = 0
			else:
				self.resistance = (0, 0)

			if self.collision_sol and self.joueur.a_sauter:
				if self.joueur.nombre_de_saut < 2:
					self.joueur.sauter()

			self.joueur.rect.clamp_ip(self.rect)
			self.gravite_jeu(self.gravite, self.resistance)
			self.joueur.mouvement(self.joueur_vitesse_x)
			self.ecran.fill((255, 255, 255))
			self.joueur.afficher(self.ecran)
			self.sol.afficher(self.ecran)
			pygame.draw.rect(self.ecran, (0, 255, 0), self.rect, 2)
			self.clock.tick(self.fps)
			pygame.display.flip()


if __name__ == '__main__':

	pygame.init()
	Jeu().boucle_principale()
	pygame.quit()
