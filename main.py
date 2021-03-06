import matplotlib as plt
import numpy as np
import math

# input: Initialisierungsliste init_list = [[v_x,v_y,v_z,phi_x,phi_y,phi_z,parent, range_v_x_min,range_v_x_max, range_v_y_min,range_v_y_max, range_v_z_min,range_v_z_max, range_phi_x_min,range_phi_x_max,  range_phi_y_min,range_phi_y_max, range_phi_z_min,range_phi_z_max,]
init_list = [[1,0,0,math.pi,0,0,-1, 0, 0, 0, 0, 0, 0, 0, math.pi, 0, 2, 0, 0],[1,0,0,math.pi,0,0,0, 0, 0, 0, 0, 0, 0, 0, math.pi, 0, 2, 0, 0],[1,0,0,math.pi,0,0,1, 0, 0, 0, 0, 0, 0, 0, math.pi, 0, 2, 0, 0]]

# Inititialisierungsliste backup (für den Reset Button um Neueingabe zu verhindern)
backup_init_list=init_list


def init_degree_of_freedom_list(init_list):
    """
init_degree_of_freedom_list erzeugt eine Liste abhängig aus Eintraegen in der init_list mit relevanten Inhalten (Freiheitsgrade).
Diese Liste ist zur Überprüfung der Range/Reichweite eines Freiheitsgrades und die Zuordnung einer Eingabe zum richtigen bewegen.
Bsp.: Der Nutzer hat ein System mit 2 Gelenken (Rotatorische Gelenke, Drehung um z-Achse möglich) initialisiert:
init_list = [[1,0,0,math.pi,0,0,-1,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -pi/2, pi/4]
                [0,1,0,math.pi,0,0,-1,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -pi/4, pi/3]]
-> degree_of_freedom_list ergibt sich: [[['phi_z',-pi/2, pi/4]][['phi_z',-pi/4, pi/3]]]
Als weitere Eintraege soll der Nutzer nun eine Liste mit Aenderungen angeben können, statt eine komplette Initialisierungsliste
-> aenderungs_liste = [[[+pi/2]],[[0]]] (das erste Gelenk soll um +pi/2 rotiert werden)
Das Programm weiß mithilfe der degree_of_freedom_list, dass der 1. eintrag zum 1. Gelenk gehoert und gleichzeitig,
dass es sich um eine Rotation um die z-Achse handelt. Zusätzlich kann hier die Range überprueft und aktualisiert werden.
Ebenso wird die Symbolik hierrüber deklariert.

    :param init_list:
    :return:

"""
    #liste aus init erzeugen, mit der anzahl innere listen = anzahl  initlist, platzhalterliste erzeugen
    len(init_list)
    degree_of_freedom_list=[[] for i in range(len(init_list))]
    for i in range(len(init_list)):
        if init_list[i][7] != 0 or init_list[i][8] != 0:
            degree_of_freedom_list[i].append(["v_x",init_list[i][7],init_list[i][8]])
        if init_list[i][9] != 0 or init_list[i][10] != 0:
            degree_of_freedom_list[i].append(["v_y",init_list[i][9],init_list[i][10]])
        if init_list[i][11] != 0 or init_list[i][12] != 0:
            degree_of_freedom_list[i].append(["v_z",init_list[i][11],init_list[i][12]])
        if init_list[i][13] != 0 or init_list[i][14] != 0:
            degree_of_freedom_list[i].append(["phi_x",init_list[i][13],init_list[i][14]])
        if init_list[i][15] != 0 or init_list[i][16] != 0:
            degree_of_freedom_list[i].append(["phi_y",init_list[i][15],init_list[i][16]])
        if init_list[i][17] != 0 or init_list[i][18] != 0:
            degree_of_freedom_list[i].append(["phi_z",init_list[i][17],init_list[i][18]])
    print(degree_of_freedom_list)
    return

"""TRANSFORMATIONSMATRIZEN AUFSTELLEN
Schritte:
1) Welche Transformationsmatrizen müssen erzeugt werden -> init_liste über die parents
"""

def init_transformationlist():
    """
    Behandelt Schritt 1) -> Erzeugt Liste aus nötigen Transformationsmatrizen
    :return: 
    """


def init_transformationmatrix(rotationsmatrix, tranVec):
    """
    Erzeugt eine homogene Transformationsmatrix 
    
    [[a_11, a_12, a_13, a_14],[a_21, a_22, a_23, a_24],[a_31, a_32, a_33, a_34][a_41, a_42, a_43, a_44]]
    
    :param rotationsmatrix: 
    :param tranVec: 
    :return: 
    
    
    Schritte:
    
    """
    #(4D-)Einheitsmatrix
    transformationsmatrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


#Rotationsmatrix um x-Achse
def












init_degree_of_freedom_list(init_list)