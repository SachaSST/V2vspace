import pygame  # necessaire pour charger les images et les sons
import random
import math 
from pygame.locals import *
pygame.init()
 
class Menu:
         
        fenetre = pygame.display.set_mode((1300, 600), )
 
        pygame.display.set_caption("Menu jeu")
 
        fond = pygame.image.load("wallpapersden.com_cool-red-mountains-4k_1600x600.jpg").convert()
        fenetre.blit(fond, (0,0))

        Bouton_2 = pygame.image.load("start_btn.png").convert_alpha()
        Bouton_2_pos = (540,450)

        Text_1_pos = (590, 390)
        font = pygame.font.Font(None, 70)
        Text_1 = font.render("START",1,((255,255,0)))
        font = pygame.font.SysFont('impact',20)
        fenetre.blit (Text_1, Text_1_pos)

 
continuer = 1
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                continuer = 0
     
    #Rafraichissement
    pygame.display.flip()
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
	
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
class Joueur() : 
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 2
        self.score = 0
        
    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score = self.score + 1

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 5
    
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0:
            self.etat = "chargee"
                
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
class Ennemi():
    NbEnnemis = 6

    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
    

