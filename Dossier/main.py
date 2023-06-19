import pygame
import math
from classes import *
from slider import *
def Get_D_and_alpha(A_xy, B_xy):
    (A_x, A_y) = A_xy
    (B_x, B_y) = B_xy
    ## application de l'echelle :
    (A_x, A_y) = (A_x*Dist_px, A_y*Dist_px)
    (B_x, B_y) = (B_x*Dist_px, B_y*Dist_px)

    ## Distance entre deux astres A et B
    D = math.sqrt(math.pow((B_y-A_y),2) + math.pow((B_x-A_x),2))

    ## Anlge entre axe x et D
    if D == 0:
        alpha = 0
    else:
        if (A_y >= B_y) and (A_x <= B_x) :
            alpha = -math.acos((B_x-A_x)/D)

        elif (A_y <= B_y) and (A_x <= B_x) :
            alpha = math.acos((B_x-A_x)/D)

        elif (A_y >= B_y) and (A_x >= B_x) :
            alpha = -math.acos((B_x-A_x)/D)

        elif (A_y <= B_y) and (A_x >= B_x) :
            alpha = math.acos((B_x-A_x)/D)


    return (D,alpha)

def Get_Vitesse(MA, MB, D, newTicks, oldTicks):

    G = 6.67430*math.pow(10,-11)
    Vb = (1/MB)* G * ((MA*MB)/math.pow(D,2)) * ((newTicks-oldTicks)/1000)
    return Vb

def Get_VBx_Vby(alpha,V):
    if V == 0 :
        return (0,0)
    else:
        VBx = -V*math.cos(alpha)
        VBy = -V*math.sin(alpha)

        return (VBx,VBy)

resolution = (1366,763)
couleur_fond = (50,50,50)
run = True
fps = 60

pygame.init()
pygame.display.init()
WIN = pygame.display.set_mode(resolution).fill((255,255,255))
pygame.display.flip()

##Boucle principale du simulateur
## Définition des caractéristiques des astres (masse, couleur, pos, vitesse)
(xmax,ymax) = resolution
Astre_A = Planet(5.9722*math.pow(10,24) ,(255,0,0),(round(xmax/2),round(ymax/2)))
Astre_B = Asteroid(1*math.pow(10,60),(0,155,0),(300,100),(3,0))

menu = Menu(WIN)
## Réculération des ticks
old_ticks = pygame.time.get_ticks()
while run:
    ## réculération des ticks
    new_ticks = pygame.time.get_ticks()
    if new_ticks > (old_ticks + (1/fps)*1000):
        ## actualisation de la fenetre et des ticks
        pygame.draw.rect(pygame.display.get_surface(), couleur_fond,pygame.Rect((0,0),resolution))


        ## dessine les astres
        Astre_A.draw(pygame.display.get_surface())
        Astre_B.draw(pygame.display.get_surface())

        ## calcul des prochaines coordonnées
        (D,alpha) = Get_D_and_alpha(Astre_A.coord_xy,Astre_B.coord_xy)
        V = Get_Vitesse(Astre_A.get_masse(),Astre_B.get_masse(),D,new_ticks,old_ticks)

        (VBx,VBy) = Get_VBx_Vby(alpha,V) #Récupération des vitesses selon les axes en m/s
        
        #conversion des vitesses en px / s
        (VBx,VBy) = (VBx/Dist_px,VBy/Dist_px)
        Astre_B.add_vitesse((VBx,VBy))
        Astre_B.move()

        #print(Astre_B.get_vitesse(), Astre_B.get_coords(),alpha)

        menu.run(Astre_A)

        ## event de fermeture de la fenetre
        pygame.display.flip()
        old_ticks = new_ticks

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Astre_A = Planet(5.9722*math.pow(10,24) ,(255,0,0),(round(xmax/2),round(ymax/2)))
                Astre_B = Asteroid(1*math.pow(10,60),(0,155,0),(300,100),(3,0))
    
        pygame.display.update()

pygame.quit()

