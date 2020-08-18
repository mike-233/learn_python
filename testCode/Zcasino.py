import math
import random

def game_f(mise,montant) :
    alea_number = random.randrange(50)
    choice_number = int(input("Vous misez sur quel nombre :"))
    if alea_number == choice_number :
        mise *=3
        print("vous avez gagné votre mise a triplé est devient ",mise)
        montant += mise
    elif alea_number%2 == choice_number%2 :
        mise = math.ceil(mise/2)
        print("Vous avez misé sur la bonne couleur donc vous obtenez la moitié de la mise ",mise)
        montant += mise
    else :
        print("Vous n'avez pas choisi le bon numéro donc vous perdez votre mise")
        montant -= mise
    return montant
    
money = 1000
print("Bienvenue sur le jeu de casino !!!!\nVous démarrez avec un montant de ",1000," $")
game = True
while game :
    mise = input("Entrez le montant de la mise : ")
    try :
        mise = int(mise)
        assert mise <=money
    except AssertionError :
        print("Le montant de la mise ne peut pas être supérieur à votre solde !!")
        continue
    except ValueError :
        print("Veillez entrer un chiffre svp ")
    a = game_f(mise,money)
    answer = input("Voulez-vous continuer ?(y/n) : ")
    while answer not in "yn" :
        answer = input("Voulez-vous continuer ?(y/n) :")
    if answer == "y" :
        game = True
    else :
        game = False
        
print("votre nouveu solde est : ",a)
