#from weapon import Weapon
class Player :
    def __init__(self,pseudo,health,attack) :
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur ",self.pseudo,"/ points de vie :",self.health,"/ attack ",self.attack)

    def get_pseudo(self) :
        return self.pseudo
    def get_health(self) :
        return self.health
    def get_attack_value(self) :
        return self.attack
    def damage(self,damage) :
        self.health -= damage
        print("Aie..... tu vient de subir ",damage," dégâts")
    def attack_player(self,target_player) :
        if self.has_weapon() : # ajoute les dégats de l'arme au point d'attaque du joueur
            target_player.damage(self.weapon.get_damage_amount()+self.attack)
        else :
            target_player.damage(self.attack)
    def set_weapon(self, weapon): # méthode pour changer l'arme du joueur
        self.weapon = weapon
    # méthode pour verifier si le joueur a une arme
    def has_weapon(self):
        return self.weapon is not None