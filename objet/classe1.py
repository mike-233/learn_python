from player import Player

player1 = Player("Mike",100,5)
player2 = Player("Bob",100,3)
print(player1.get_pseudo()," attaque ",player2.get_pseudo())
player1.attack_player(player2)
print("Bienvenue ",player1.get_pseudo()," / points de vie ",player1.get_health()," / attaque ",player1.get_attack_value())
print("Bienvenue ",player2.get_pseudo()," / points de vie ",player2.get_health()," / attaque ",player2.get_attack_value())