import pygame
from game import Game
pygame.init()
        
#Generer la fenetre de notre jeu
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080,700))

background = pygame.image.load("assets/bg.jpg")
#on charge notre jeu
game = Game()
running = True
#Boucle tant que la condition est vrai
while running :
    #Appliquer l'arriére plan de notre jeu
    screen.blit(background,(0,-200))
    #Appliquer l'image d'un joueur
    screen.blit(game.player.image,game.player.rect)
    #verifie si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0 :
        game.player.move_left()
    #Mettre à jour de l'ecran
    pygame.display.flip()
    
    for event in pygame.event.get() :  
        #Que l'événement est fermeture de la fenêtre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #si un joueur lache une touhe du clavier
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False