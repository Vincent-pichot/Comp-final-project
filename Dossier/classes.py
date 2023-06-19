import pygame
import math
##Echelle :
#Dist_px = 6666667; #1px = 6 666 667 m
Dist_px = 1000

class Planet:

    def __init__(self,masse,couleur,coord_xy):
        self.masse = masse #en KG
        self.couleur = couleur
        self.coord_xy = coord_xy
        pass

    def draw(self,surface):
        radius = round((60*self.masse)/(5.9722*math.pow(10,24)))
        pygame.draw.circle(surface, self.couleur, self.coord_xy, radius)
        pass

    def set_masse(self,masse):
        self.masse = masse
        pass

    def get_masse(self):
        return self.masse
        pass

    def set_coords(self,coords):
        self.coord_xy = coords
        pass

    def get_coords(self):
        return self.coord_xy
        pass


class Asteroid:

    def __init__(self,masse,couleur,coord_xy,vitesse_vx_vy):
        self.masse = masse #en KG
        self.couleur = couleur
        self.coord_xy = coord_xy
        self.vitesse_vx_vy = vitesse_vx_vy
        pass

    def draw(self,surface):
        (x,y) = self.coord_xy
        radius = 30
        pygame.draw.ellipse(surface, self.couleur,pygame.Rect(x-radius,y-(radius/2),radius*2,(radius/2)*2))
        pass

    def set_masse(self,masse):
        self.masse = masse
        pass

    def get_masse(self):
        return self.masse
        pass

    def set_coords(self,coords):
        self.coord_xy = coords
        pass

    def get_coords(self):
        return self.coord_xy
        pass

    def get_vitesse(self):
        return self.vitesse_vx_vy
        pass

    def add_vitesse(self,vitesseXY):

        (oldVx,oldVy) = self.vitesse_vx_vy
        (newVx,newVy) = vitesseXY
        self.vitesse_vx_vy = (oldVx+newVx,oldVy+newVy)
        pass

    def move(self):
        (oldX,oldY) = self.coord_xy
        (Vx,Vy) = self.vitesse_vx_vy
        (newX,newY) = (oldX+math.floor(Vx),oldY+math.floor(Vy))
        self.coord_xy=(newX,newY)
        pass