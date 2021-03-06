import math

class Obstacle :
    #les verifications se font par rapport au nom O = Obstacle rond et C = Obstacle Carre
    def __init__(self,x,y,z=0,nom='O',r=1.0,lo=0.0,la=0.0):        #Initialisation des arguments
        self._nom=nom
        self._x=x
        self._y=y
        self._z=z
        self._r=r
        self._lo=lo
        self._la=la

    def est_dans(self,x,y,z):                                       #On vérifie si l'objet de coordonées x,y,z se trouve dans l'obstacle
        if (self._nom=='C'):                                        #Si c'est un rectangle
            x1=self._x                                              #x1 ,x2 , y1 et y2 représentent les quatres points du rcetangle(Carre)
            x2=self._x + self._lo
            y1=self._y
            y2=self._y - self._la
            return x>=x1 and x<= x2 and y<=y1 and y>=y2             #Si les coordonées de l'objet touchent le rectangle ou sont dedans
        if (self._nom=='O'):                                        #Pour un obstacle Rond
            return (x-self._x)**2+(y-self._y)**2 <= self._r**2      #On verifie si les coordonées de l'objet se trouvent dans le cercle

    def __str__(self):
        return ""

    def getColor(self):
        pass

class ObstacleCarre(Obstacle):

    def __init__(self,x,y,z=0,lo=0.0,la=0.0,couleur="blue"):                 #Initialisation des arguments
        self._x=x
        self._y=y
        self._z=z
        self._lo=lo
        self._la=la
        self.name = 'C'
        self.color=couleur

    def est_dans(self,x,y,z):                                       #On vérifie si le point de coordonées x,y,z se trouve dans l'obstacle
        x1=self._x                                                  #x1 ,x2 , y1 et y2 représentent les quatres points du rcetangle(Carre)
        x2=self._x + self._lo
        y1=self._y
        y2=self._y - self._la
        return x>=x1 and x<= x2 and y<=y1 and y>=y2                 #Si les coordonées de l'objet touchent le rectangle ou sont dedans

    def __str__(self):
        return "C"+" "+str(self._x)+" "+str(self._y)+" "+str(self._z)+" "+str(self._lo)+" "+str(self._la)+" "+str(self.color)

    def getColor(self):
        return self.color

class ObstacleRond(Obstacle):
    def __init__(self,x,y,z=0,r=1.0,couleur='red'):                               #Initialisation des arguments
        self._x=x
        self._y=y
        self._z=z
        self._r=r
        self.name = 'R'
        self.color=couleur

    def est_dans(self,x,y,z):                                       #On vérifie si l'objet de coordonées x,y,z se trouve dans l'obstacle
        return (x-self._x)**2+(y-self._y)**2 <= self._r**2          #On verifie si les coordonées du point se trouvent dans le cercle

    def __str__(self):

        return "O"+" "+str(self._x)+" "+str(self._y)+" "+str(self._z)+" "+str(self._r)+" "+str(self.color)
    def getColor(self):
        return self.color

class ObstacleBalise(Obstacle):
    def __init__(self,x,y,z=0,lo=0.0,la=0.0,haut=0.0,color1='blue',color2='red',color3='yellow',color4='green'):
        self._x=x
        self._y=y
        self._z=z
        self.lo=lo                                                                      #Initialisation des arguments
        self.la=la                                                                      #avec pour obligationdavoir
        self.haut=haut                                                                  #les couleurattribue
        self.color1=color1
        self.color2=color2
        self.color3=color3
        self.color4=color4

    def est_dans(self,x,y,z):
        x1=self._x
        x2=self._x+self.lo                                                              #nous verifions si la position
        y1=self._y                                                                      #est bien sur la balise
        y2=self._y+self.la
        z1=self._z
        z2=self._z=self.haut
        return x>=x1 and x<=x2 and y<=y1 and y>=y2 and z>=z1 and z<=z2


    def getColor(self,x,y,z):
        if (x>self._x) and (x<self._x+self.lo/2):                                           #nous vérifions la position dans l'obstacle de la coordonées
            if (y>self._y) and (y<self._y+self.la/2):                                       #puis on retourne la couleur en fonction de la position dans l'obstacle
                return self.color1
            elif (y>self._y+self.la/2) and (y<self._y+self.lo):
                return self.color3
            else :
                print("Cette coordonee n'existe pas (y est faux)")
                return 1
        elif(x>self._x+self.lo/2) and (x<self._x+self.lo):
            if (y>self._y) and (y<self._y+self.la/2):
                return self.color2
            elif (y>self._y+self.la/2) and (y<self._y+self.lo):
                return self.color4
            else :
                print("Cette coordonee n'existe pas (y est faux)")
                return 1
        else:
            print("Cette coordonee n'existe pas (x est faux)")
            return 1



    def __str__(self):
        return "B"+" "+str(self._x)+" "+str(self._y)+" "+str(self._z)+" "+str(self.lo)+" "+str(self.la)+" "+str(self.color1)+" "+str(self.color2)+" "+str(self.color3)+" "+str(self.color4)


    #str retourne une façons particuliere
    #une chaine de caractere
    #pour lecriture.Envoie les donnees de la balise
