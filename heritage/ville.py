class Batiment :
    def __init__(self,adresse,nb_etage) :
        self.adresse = adresse
        self.nb_etage = nb_etage
        
    def get_adresse(self) :
        return self.adresse
    
    def get_nb_etage(self) :
        return self.nb_etage
    
class Immeuble(Batiment) :
    def __init__(self,adresse,nb_etage,nb_balcons) :
        super().__init__(adresse,nb_etage)
        self.nb_balcons = nb_balcons
        
class Supermarket(Batiment) :
    def __init__(self,adresse,nb_etage,nb_rayons) :
        super().__init__(adresse,nb_etage)
        self.nb_rayons = nb_rayons
    def get_nb_rayons(self) :
        return self.nb_rayons   
class Banque(Batiment) :
    def __init__(self,adresse,nb_etage,nb_coffres,nom) :
        super().__init__(adresse,nb_etage)  # ou Batiment.__init__(self,adresse,nb_etage)
        self.nb_coffres = nb_coffres
        self.nom = nom
    def get_nb_coffres(self) :
        return self.nb_coffres
    def get_nom(self) :
        return self.nom
            
# 4 Immeuble          
immeuble1 = Immeuble("Touba",3,6)
immeuble2 = Immeuble("Sacre coeur",50,100)
immeuble3 = Immeuble("Almadies",90,180)
immeuble4 = Immeuble("Cité Keur Khadim",9,19)

#2 marché
supermarket1 = Supermarket("Castor",3,200)
supermarket2 = Supermarket("VDN",8,500)

#Une banque
banque = Banque("Place de l'indépense",20,9,"Freedom")
