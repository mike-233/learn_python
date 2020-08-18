from player import Player
from weapon import Weapon

knife = Weapon("Couteau",3)
arme1 = Weapon("Kalachnicof",10)
player1 = Player("Mike",100,5)
player2 = Player("Bob",100,3)

player1.set_weapon(arme1)
player2.set_weapon(knife)

print(player1.get_pseudo()," attaque ",player2.get_pseudo())
player1.attack_player(player2)
print(player1.get_pseudo()," attaque ",player2.get_pseudo())
player2.attack_player(player1)

print("Bienvenue ",player1.get_pseudo()," / points de vie ",player1.get_health()," / attaque ",player1.get_attack_value())
print("Bienvenue ",player2.get_pseudo()," / points de vie ",player2.get_health()," / attaque ",player2.get_attack_value())

print("Verification de la presence d'une arme")
print(player1.has_weapon())
print(player2.has_weapon())