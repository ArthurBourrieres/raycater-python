import math

import pygame as pg
import pygame
from math import *
import random

l_scr = 640
h_scr = 320

x_joueur = 80
y_joueur = 80
vecteur_x, vecteur_y = 0, 0
vitesse = 5

point = ()

fov =5
angle_vision = 0
ecart_point = (3/5)*fov
nm_point = 640/fov
liste_point = []
sprit = [[200, 100, 10]]

pg.init()
SCR = pg.display.set_mode((l_scr, h_scr))
SCR2 = pg.display.set_mode((l_scr, h_scr))
Clock = pg.time.Clock()
run = True
first = True
avencer = True
reculer = True

_ = False

map_schema = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,1,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,1,1,1,1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
map = []
liste_distance = []
conteur_switch = 51
affichage_map = None


def chargement_map():
    global map

    for y, i in enumerate(map_schema):
        for x, a in enumerate(i):
            if a == 1:
                map.append([x, y])

def deplacement_joueur():
    global x_joueur, y_joueur, zoom, angle_max, angle_min, affichage_map, conteur_switch, point, angle_vision, reculer, avencer, vecteur_x, vecteur_y

    vecteur_x = 2*cos(radians(angle_vision))
    vecteur_y = 2*sin(radians(angle_vision))
    point = (x_joueur+(vecteur_x*5), y_joueur+(vecteur_y*5))

    case_x = point[0]//40
    case_y = point[1]//40
    avencer = True
    reculer = True

    if map_schema[int(case_y)][int(case_x)] == 1:
        avencer = False

    if Keys[pygame.K_d]:
        x_joueur += vitesse
    if Keys[pygame.K_q]:
        x_joueur -= vitesse
    if Keys[pygame.K_z] and avencer:
        x_joueur += vecteur_x
        y_joueur += vecteur_y
    if Keys[pygame.K_s] and reculer:
        x_joueur -= vecteur_x
        y_joueur -= vecteur_y
    if Keys[pygame.K_RIGHT]:
        angle_vision += 5
    if Keys[pygame.K_LEFT]:
        angle_vision -= 5

    if Keys[pygame.K_e]:
        conteur_switch += 1
        affichage_map = conteur_switch%2

def plot():
    SCR.fill("black")
    pygame.draw.rect(SCR, "lightblue", [0, 0, 640, 160])
    if affichage_map == 0:
        for i in map:
            pygame.draw.rect(SCR2, "grey", [i[0]*40, i[1]*40, 40, 40])
        pygame.draw.circle(SCR2, "red", [x_joueur, y_joueur], 5)
        pg.draw.line(SCR2, "yellow", [x_joueur, y_joueur], point)

        for i in sprit:
            pygame.draw.circle(SCR2, 'green', ([i[0], i[1]]), i[2])


    if affichage_map == 1:
        for colone, distance in enumerate(liste_distance):

            hauteur = 1 * (h_scr/distance)
            hauteur *= 40
            y1 = int(h_scr/2 - (hauteur/2))
            y2 = int(h_scr / 2 + (hauteur / 2))
            pg.draw.rect(SCR, "darkgrey", [colone*fov, y1, fov, y2-y1])
 






def ray():
    global x_joueur, y_joueur, map_schema, angle_min, angle_max, liste_distance, vecteur_x, vecteur_y, angle_a

    for i in range(1, int(nm_point+1)):
        ligne_y = -(nm_point / 2 * ecart_point)
        ligne_y += i * ecart_point

        liste_point.append([200, ligne_y])

    for i in liste_point:
        i[0], i[1] = i[0] * cos(radians(angle_vision)) - i[1] * sin(radians(angle_vision)), i[0] * sin(radians(angle_vision)) + i[1] * cos(radians(angle_vision))

        vecteur_point_x = i[0]/ 200
        vecteur_point_y = i[1]/ 200
        contacte = True
        point_x = x_joueur
        point_y = y_joueur
        while contacte:
            case_x = point_x // 40
            case_y = point_y // 40

            for i in sprit:
                if math.sqrt((i[0]-point_x)**2+(i[1]-point_y)**2) < i[2]:
                    distance_sprit = math.sqrt((i[0]-x_joueur)**2+(i[1]-y_joueur)**2)
                    pygame.draw.line(SCR2, "yellow", [x_joueur, y_joueur], [point_x, point_y])
                    contacte = False



            if map_schema[int(case_y)][int(case_x)] == 1:

                contacte = False

            point_x += vecteur_point_x
            point_y += vecteur_point_y


        distance = sqrt((x_joueur - point_x) ** 2 + (y_joueur - point_y) ** 2)

        liste_distance.append(distance)

def mouve_sprit():
    global sprit

    for i in sprit:
        i[0] += 1
        i[1] += 0

while True:
    Keys = pg.key.get_pressed()
    if first:
        chargement_map()
    deplacement_joueur()

    liste_point = []
    mouve_sprit()
    plot()
    liste_distance = []
    ray()

    time = Clock.tick(60) / 1000
    time = 1/time

    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()


    pygame.display.set_caption(str(time))
    first = False