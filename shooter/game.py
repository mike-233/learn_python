import pygame
from player import Player

class Game :
    def __init__(self) :
        #charger notre joueur
        self.player = Player()
        self.pressed = {
            "touche_fleche_droite" : True,
            "touche_fleche_gauche" : False
        }