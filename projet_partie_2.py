"""CAVARO.A & LAMOULEN.L"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time

'''
Partie 2
--------

train = transporte conteneurs de marchandises

départ = site industriel entreprise 1
arrivé = site industriel entreprise 2

conteneurs longueur = 11,583 mètres
conteneurs largeur = 2,294 mètres
conteneur hauteur = 2,569 mètres

transport = 1 conteneur par wagon

problème = determiner affectation marchandises dans les conteneurs
but = minimiser le nombre total de wagons

caracteristique des marchandises disponible dans donneesmarchandises.


d = dimension du problème

d1 = prise en compte seulement de la longueur des marchandises.
d1 = Marchandises = segments de droite #  non côte à côte, non superposer.
d1 = longueur

d2 = prise en compte de la surface occupée au sol par les marchandises
d2 = marchandises côte à côte si on veut # pas de superposition en hauteur
d2 = longueur + largeur

d3 = volume occupé par marchandise
d3 on peut les empiler si on veut
d3 = longueur + largeur + hauteur

2 cas possible suivant si on trie ou non marchandise :

Off line = trier les marchandises avant de les charger dans les conteneurs

On line = marchandises ne peuvent pas être triées
marchandise = premier arrivé premier affectée (pile)
'''


marchandises = [
    {"Numéro": 1, "Désignation": "Tubes acier", "Longueur": 10, "Largeur": 1, "Hauteur": 0.5},
    {"Numéro": 2, "Désignation": "Tubes acier", "Longueur": 9, "Largeur": 2, "Hauteur": 0.7},
    {"Numéro": 3, "Désignation": "Tubes acier", "Longueur": 7.5, "Largeur": 1.2, "Hauteur": 0.4},
    {"Numéro": 4, "Désignation": "Acide chlorhydrique", "Longueur": 1, "Largeur": 1, "Hauteur": 1},
    {"Numéro": 5, "Désignation": "Godet pelleteuse", "Longueur": 2, "Largeur": 2, "Hauteur": 1},
    {"Numéro": 6, "Désignation": "Rails", "Longueur": 11, "Largeur": 1, "Hauteur": 0.2},
    {"Numéro": 7, "Désignation": "Tubes PVC", "Longueur": 3, "Largeur": 2, "Hauteur": 0.6},
    {"Numéro": 8, "Désignation": "Echaffaudage", "Longueur": 3, "Largeur": 1.3, "Hauteur": 1.8},
    {"Numéro": 9, "Désignation": "Verre", "Longueur": 3, "Largeur": 2.1, "Hauteur": 0.6},
    {"Numéro": 10, "Désignation": "Ciment", "Longueur": 4, "Largeur": 1, "Hauteur": 0.5},
    {"Numéro": 11, "Désignation": "Bois vrac", "Longueur": 5, "Largeur": 0.8, "Hauteur": 1},
    {"Numéro": 12, "Désignation": "Troncs chênes", "Longueur": 6, "Largeur": 1.9, "Hauteur": 1},
    {"Numéro": 13, "Désignation": "Troncs hêtres", "Longueur": 7, "Largeur": 1.6, "Hauteur": 1.5},
    {"Numéro": 14, "Désignation": "Pompe à chaleur", "Longueur": 5, "Largeur": 1.1, "Hauteur": 2.3},
    {"Numéro": 15, "Désignation": "Cuivre", "Longueur": 6, "Largeur": 2, "Hauteur": 1.4},
    {"Numéro": 16, "Désignation": "Zinc", "Longueur": 5, "Largeur": 0.8, "Hauteur": 0.8},
    {"Numéro": 17, "Désignation": "Papier", "Longueur": 4, "Largeur": 1.6, "Hauteur": 0.6},
    {"Numéro": 18, "Désignation": "Carton", "Longueur": 7, "Largeur": 1, "Hauteur": 1.3},
    {"Numéro": 19, "Désignation": "Verre blanc vrac", "Longueur": 9, "Largeur": 0.9, "Hauteur": 2.2},
    {"Numéro": 20, "Désignation": "Verre brun vrac", "Longueur": 3, "Largeur": 1.6, "Hauteur": 0.9},
    {"Numéro": 21, "Désignation": "Briques rouges", "Longueur": 5, "Largeur": 1.1, "Hauteur": 2.4},
    {"Numéro": 22, "Désignation": "Pièces métalliques", "Longueur": 6, "Largeur": 1.6, "Hauteur": 1.4},
    {"Numéro": 23, "Désignation": "Pièces métalliques", "Longueur": 7, "Largeur": 0.9, "Hauteur": 1.2},
    {"Numéro": 24, "Désignation": "Pièces métalliques", "Longueur": 3, "Largeur": 1.6, "Hauteur": 1.9},
    {"Numéro": 25, "Désignation": "Ardoises", "Longueur": 1, "Largeur": 1.8, "Hauteur": 1},
    {"Numéro": 26, "Désignation": "Tuiles", "Longueur": 2, "Largeur": 1.2, "Hauteur": 2.3},
    {"Numéro": 27, "Désignation": "Vitraux", "Longueur": 4, "Largeur": 0.7, "Hauteur": 1.2},
    {"Numéro": 28, "Désignation": "Carrelage", "Longueur": 6, "Largeur": 1.2, "Hauteur": 2.5},
    {"Numéro": 29, "Désignation": "Tôles", "Longueur": 7, "Largeur": 0.6, "Hauteur": 1.5},
    {"Numéro": 30, "Désignation": "Tôles", "Longueur": 9, "Largeur": 1.7, "Hauteur": 1},
    {"Numéro": 31, "Désignation": "Tôles", "Longueur": 6, "Largeur": 1.9, "Hauteur": 1.6},
    {"Numéro": 32, "Désignation": "Tôles", "Longueur": 3, "Largeur": 2.2, "Hauteur": 2.2},
    {"Numéro": 33, "Désignation": "Tôles", "Longueur": 3, "Largeur": 0.5, "Hauteur": 2.2},
    {"Numéro": 34, "Désignation": "Mobilier urbain", "Longueur": 4, "Largeur": 0.7, "Hauteur": 1.9},
    {"Numéro": 35, "Désignation": "Lin", "Longueur": 5, "Largeur": 2.2, "Hauteur": 0.7},
    {"Numéro": 36, "Désignation": "Textiles à recycler", "Longueur": 6, "Largeur": 1.3, "Hauteur": 2.5},
    {"Numéro": 37, "Désignation": "Aluminium", "Longueur": 6, "Largeur": 1.3, "Hauteur": 1.2},
    {"Numéro": 38, "Désignation": "Batteries automobile", "Longueur": 7, "Largeur": 1.4, "Hauteur": 2.5},
    {"Numéro": 39, "Désignation": "Quincaillerie", "Longueur": 6, "Largeur": 1.1, "Hauteur": 1},
    {"Numéro": 40, "Désignation": "Treuil", "Longueur": 7, "Largeur": 0.9, "Hauteur": 1.3},
    {"Numéro": 41, "Désignation": "Treuil", "Longueur": 8, "Largeur": 0.5, "Hauteur": 0.5},
    {"Numéro": 42, "Désignation": "Acier", "Longueur": 8, "Largeur": 0.9, "Hauteur": 1.7},
    {"Numéro": 43, "Désignation": "Laine de bois", "Longueur": 8, "Largeur": 0.9, "Hauteur": 1.8},
    {"Numéro": 44, "Désignation": "Ouate de cellulose", "Longueur": 5, "Largeur": 1.7, "Hauteur": 1.2},
    {"Numéro": 45, "Désignation": "Chanvre isolation", "Longueur": 2.2, "Largeur": 1.6, "Hauteur": 1.1},
    {"Numéro": 46, "Désignation": "Moteur électrique", "Longueur": 4.2, "Largeur": 1.5, "Hauteur": 0.8},
    {"Numéro": 47, "Désignation": "Semi conducteurs", "Longueur": 3.7, "Largeur": 0.9, "Hauteur": 1.4},
    {"Numéro": 48, "Désignation": "Semi conducteurs", "Longueur": 5.6, "Largeur": 0.5, "Hauteur": 1.4},
    {"Numéro": 49, "Désignation": "Semi conducteurs", "Longueur": 4.9, "Largeur": 0.9, "Hauteur": 2.5},
    {"Numéro": 50, "Désignation": "Semi conducteurs", "Longueur": 8.7, "Largeur": 1.3, "Hauteur": 1.3},
    {"Numéro": 51, "Désignation": "Semi conducteurs", "Longueur": 6.1, "Largeur": 2.2, "Hauteur": 2.3},
    {"Numéro": 52, "Désignation": "Semi conducteurs", "Longueur": 3.3, "Largeur": 1.8, "Hauteur": 2.3},
    {"Numéro": 53, "Désignation": "Semi conducteurs", "Longueur": 2.6, "Largeur": 1.6, "Hauteur": 2.3},
    {"Numéro": 54, "Désignation": "Semi conducteurs", "Longueur": 2.9, "Largeur": 1.6, "Hauteur": 2},
    {"Numéro": 55, "Désignation": "Aluminium", "Longueur": 2, "Largeur": 1.1, "Hauteur": 0.6},
    {"Numéro": 56, "Désignation": "Aluminium", "Longueur": 3, "Largeur": 0.6, "Hauteur": 1.2},
    {"Numéro": 57, "Désignation": "Aluminium", "Longueur": 6, "Largeur": 1, "Hauteur": 0.8},
    {"Numéro": 58, "Désignation": "Aluminium", "Longueur": 5, "Largeur": 1.3, "Hauteur": 0.6},
    {"Numéro": 59, "Désignation": "Aluminium", "Longueur": 4, "Largeur": 2.1, "Hauteur": 2.1},
    {"Numéro": 60, "Désignation": "Aluminium", "Longueur": 6, "Largeur": 1.5, "Hauteur": 1.9},
    {"Numéro": 61, "Désignation": "Aluminium", "Longueur": 4, "Largeur": 0.8, "Hauteur": 2.1},
    {"Numéro": 62, "Désignation": "Aluminium", "Longueur": 2, "Largeur": 2, "Hauteur": 2.3},
    {"Numéro": 63, "Désignation": "Aluminium", "Longueur": 4, "Largeur": 1, "Hauteur": 1.1},
    {"Numéro": 64, "Désignation": "Aluminium", "Longueur": 6, "Largeur": 1.8, "Hauteur": 1.1},
    {"Numéro": 65, "Désignation": "Lithium", "Longueur": 6, "Largeur": 1.9, "Hauteur": 0.9},
    {"Numéro": 66, "Désignation": "Lithium", "Longueur": 3, "Largeur": 2, "Hauteur": 2.2},
    {"Numéro": 67, "Désignation": "Lithium", "Longueur": 4, "Largeur": 1.5, "Hauteur": 0.9},
    {"Numéro": 68, "Désignation": "Lithium", "Longueur": 4, "Largeur": 2.1, "Hauteur": 2.5},
    {"Numéro": 69, "Désignation": "Lithium", "Longueur": 2, "Largeur": 1.2, "Hauteur": 1.5},
    {"Numéro": 70, "Désignation": "Lithium", "Longueur": 6, "Largeur": 1.3, "Hauteur": 2},
    {"Numéro": 71, "Désignation": "Lithium", "Longueur": 2, "Largeur": 0.8, "Hauteur": 1.1},
    {"Numéro": 72, "Désignation": "Contreplaqué", "Longueur": 4, "Largeur": 1.4, "Hauteur": 2},
    {"Numéro": 73, "Désignation": "Contreplaqué", "Longueur": 5, "Largeur": 0.6, "Hauteur": 0.5},
    {"Numéro": 74, "Désignation": "Contreplaqué", "Longueur": 5, "Largeur": 0.6, "Hauteur": 1.8},
    {"Numéro": 75, "Désignation": "Contreplaqué", "Longueur": 4, "Largeur": 0.7, "Hauteur": 1.4},
    {"Numéro": 76, "Désignation": "Contreplaqué", "Longueur": 6, "Largeur": 0.5, "Hauteur": 0.7},
    {"Numéro": 77, "Désignation": "Contreplaqué", "Longueur": 3, "Largeur": 1.5, "Hauteur": 1.8},
    {"Numéro": 78, "Désignation": "Contreplaqué", "Longueur": 3, "Largeur": 1.4, "Hauteur": 2},
    {"Numéro": 79, "Désignation": "Contreplaqué", "Longueur": 3, "Largeur": 2, "Hauteur": 2.3},
    {"Numéro": 80, "Désignation": "Contreplaqué", "Longueur": 5, "Largeur": 1.5, "Hauteur": 0.7},
    {"Numéro": 81, "Désignation": "Contreplaqué", "Longueur": 5, "Largeur": 2.2, "Hauteur": 0.5},
    {"Numéro": 82, "Désignation": "Contreplaqué", "Longueur": 6, "Largeur": 1.2, "Hauteur": 1.2},
    {"Numéro": 83, "Désignation": "Poutre", "Longueur": 5, "Largeur": 0.8, "Hauteur": 0.7},
    {"Numéro": 84, "Désignation": "Poutre", "Longueur": 3, "Largeur": 0.5, "Hauteur": 1.9},
    {"Numéro": 85, "Désignation": "Poutre", "Longueur": 5, "Largeur": 1.4, "Hauteur": 0.7},
    {"Numéro": 86, "Désignation": "Poutre", "Longueur": 6, "Largeur": 0.7, "Hauteur": 0.7},
    {"Numéro": 87, "Désignation": "Poutre", "Longueur": 6, "Largeur": 1.2, "Hauteur": 2},
    {"Numéro": 88, "Désignation": "Poutre", "Longueur": 3, "Largeur": 1.7, "Hauteur": 1.1},
    {"Numéro": 89, "Désignation": "Poutre", "Longueur": 5, "Largeur": 1.6, "Hauteur": 2.1},
    {"Numéro": 90, "Désignation": "Pneus", "Longueur": 3, "Largeur": 1.3, "Hauteur": 1.7},
    {"Numéro": 91, "Désignation": "Pneus", "Longueur": 4, "Largeur": 1.5, "Hauteur": 1.7},
    {"Numéro": 92, "Désignation": "Pneus", "Longueur": 3, "Largeur": 1.5, "Hauteur": 1.9},
    {"Numéro": 93, "Désignation": "Pneus", "Longueur": 3, "Largeur": 0.6, "Hauteur": 1.9},
    {"Numéro": 94, "Désignation": "Pneus", "Longueur": 5, "Largeur": 1.8, "Hauteur": 0.5},
    {"Numéro": 95, "Désignation": "Pneus", "Longueur": 3, "Largeur": 1.8, "Hauteur": 0.7},
    {"Numéro": 96, "Désignation": "Pneus", "Longueur": 4, "Largeur": 1.7, "Hauteur": 1.4},
    {"Numéro": 97, "Désignation": "Pneus", "Longueur": 4, "Largeur": 1.5, "Hauteur": 0.5},
    {"Numéro": 98, "Désignation": "Pneus", "Longueur": 2, "Largeur": 2.1, "Hauteur": 1.8},
    {"Numéro": 99, "Désignation": "Pneus", "Longueur": 2, "Largeur": 0.7, "Hauteur": 1.1},
    {"Numéro": 100, "Désignation": "Pneus", "Longueur": 6, "Largeur": 1.2, "Hauteur": 1.3}
]

"""Question 1"""

"""Mettrez au point un algorithme qui renvoie au moins une solution. Cet algorithme pourra être un
algorithme exact ou heuristique en fonction de la complexité du problème. Stocker les résultats
pour les challenges."""


def nb_wagons_offline_d1(marchandises, wagon_longueur=11.583):
    dico = sorted(marchandises, key=lambda x: x["Longueur"], reverse=True)
    wagons = []
    for i in dico:
        for j in wagons:
            if sum(j) + i["Longueur"] <= wagon_longueur:
                j.append(i["Longueur"])
                break
        else:
            wagons.append([i["Longueur"]])
    return len(wagons)

'''
d1 = prise en compte seulement de la longueur des marchandises.
d1 = Marchandises = segments de droite #  non côte à côte, non superposer.
d1 = longueur
On line = marchandises ne peuvent pas être triées
marchandise = premier arrivé premier affectée (pile)

Algorithme papier:

    parcourir longueurs de mes objets
        parcourir mes wagons
            utilisation boucle for
                si on a de la place on met
        si liste objet pas vide
            wagon +=1
'''


def nb_wagons_online_d1(dico, wagon_longueur=11.583):
    wagons = []
    for i in dico:
        for j in wagons:
            if sum(j) + i["Longueur"] <= wagon_longueur:
                j.append(i["Longueur"])# on ajoute la longueur de l'objet dans le wagon
                break
        else:
            wagons.append([i["Longueur"]]) # il y a [i["Longueur"]] car on ne peut pas mettre un int dans une liste donc ce qui rentre dans la liste est une liste
    return len(wagons), wagons



'''
d2 = prise en compte de la surface occupée au sol par les marchandises
d2 = marchandises côte à côte si on veut # pas de superposition en hauteur
d2 = longueur + largeur
On line = marchandises ne peuvent pas être triées
marchandise = premier arrivé premier affectée (pile)
conteneurs longueur = 11,583 mètres
conteneurs largeur = 2,294 mètres

Le but ici est d'utiliser la méthode shelf pour placer les objets dans les wagons via l'utilisation de niveaux de hauteur

Pour essayer de réduire l'espace perdu, Shelf First Fit parcourt chaque étagère pour chaque nouvelle marchandise.
Il insère la marchandise dans la première étagère avec de l'espace disponible (créant une nouvelle étagère si aucune étagère existante n'a de place).
La méthode Best Fit est similaire à SHELF-FF, mais au lieu de choisir la première étagère avec de l'espace, elle choisit l'étagère la plus petite horizontalement avec suffisamment d'espace pour la marchandise.

Le but ici est de placer les objets dans les wagons en utilisant la largeur des étagères pour minimiser l'espace perdu avec la méthode shelf
et d'utiliser la méthode Best Fit pour placer les objets dans les wagons en utilisant la hauteur des étagères pour minimiser l'espace perdu.

Algorithme Shelf First Fit Decreasing :

1. Trier les marchandise par leurs largeurs et longueurs en ordre décroissant. je place les marchandise qui prennent le plus de place en premier.
2. Initialiser une liste de wagons vide.
3. Pour chaque marchandise triée, je parcours la liste des wagons existants
4. Pour chaque wagon, je parcours les étagères existantes
5. Je vérifie si la marchandise rentre sur une étagère existante c'est à dire que j'observe la largeur et la longueur de l'étagère (la largeur de l'étagère est celle de la marchandise ayant la largeur max et la longueur de l'étagère correspond à la longueur des objets qu'elle possède + l'objet qu'on souhaite placer et il faut qu'il reste inférieur ou égale a la longueur du wagon)
6. Si la marchandise à une largeur inférieur à l'étagère, et que l'addition de sa longueur à celle de l'étagère est inférieur ou égale à la longueur du wagon alors on l'ajoute à l'étagère
6. Si la marchandise ne rentre pas sur une étagère existante, je vérifie si la marchandise rentre dans le wagon
7. Je vérifie que la somme de la largeur de mes étagère + la largeur de ma marchandise est inférieur à la largeur de mon wagon .
8. Si c'est le cas, je crée une nouvelle étagère dans le wagon et j'y place la marchandise cette nouvelle étagère sera au dessus de la dernière étagère créée et prendra comme longueur la longueur de l'item et comme largeur la largeur de la marchandise.
8. Si on ne peut plus placer d'étagère dans le wagon, je crée un nouveau wagon et j'y place la marchandise ainsi qu'une étagère ayant pour longueur la longueur de la marchandise et pour largeur la largeur de la marchandise.
9. Je retourne le nombre de wagon utilisé.
'''              

def nb_wagons_offline_d2(dico, wagon_longueur=11.583, wagon_largeur=2.294):
    wagons = [] # initialisation a vide qui va nous permettre de stocker les wagons et leurs contenus
    #wagon est une liste et chaque élément de cette liste est un dictionnaire qui contient la longueur, la largeur et les items de l'étagère
    dico = sorted(dico, key=lambda x: (x["Largeur"], x["Longueur"]), reverse=True)# tri des marchandises par largeur et longueur en ordre décroissant
    
    for item in dico:  # Parcours de chaque marchandise du dico
        placed = False # initialisation de la variable placed à False
        for wagon in wagons:  # Parcours des wagons
            for shelf in wagon:  # Parcours des étagères dans un wagon
                if item["Largeur"] <= shelf["Largeur"] and (shelf["Longueur"] + item["Longueur"]) <= wagon_longueur: #Si la largeur de l'item est inférieure ou égale à la largeur de l'étagère et sa longueur plus la longueur actuelle de l'étagère est inférieure ou égale à la longueur du wagon alors on l'ajoute à l'étagère
                    # Ajout de l'item à l'étagère existante
                    shelf["Longueur"] += item["Longueur"] # on ajoute la longueur de l'item à la longueur de l'étagère
                    shelf["Items"].append(item) # on ajoute l'item à la liste des items de l'étagère
                    placed = True
                    break
            if placed:
                break

            # Si la marchandise ne peut pas être placée sur les étagères existantes, on essaie de créer une nouvelle étagère
            total_shelf_width = sum(s["Largeur"] for s in wagon)
            if (total_shelf_width + item["Largeur"]) <= wagon_largeur:
                # Ajout d'une nouvelle étagère
                wagon.append({"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Items": [item]})
                placed = True
                break

        if not placed:
            # Si la marchandise n'a pas pu être placée dans les wagons existants, on crée un nouveau wagon
            wagons.append([{"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Items": [item]}])

    return wagons, len(wagons)


def nb_wagons_online_d2(dico, wagon_longueur=11.583, wagon_largeur=2.294):
    wagons = []
    
    for item in dico:  # Parcours des marchandises
        placed = False
        for wagon in wagons:  # Parcours des wagons
            for shelf in wagon:  # Parcours des étagères dans un wagon
                if item["Largeur"] <= shelf["Largeur"] and (shelf["Longueur"] + item["Longueur"]) <= wagon_longueur:
                    # Ajout de l'item à l'étagère existante
                    shelf["Longueur"] += item["Longueur"]
                    placed = True
                    break
            if placed:
                break

            # Si la marchandise ne peut pas être placée sur les étagères existantes, on essaie de créer une nouvelle étagère
            total_shelf_width = sum(s["Largeur"] for s in wagon)
            if (total_shelf_width + item["Largeur"]) <= wagon_largeur:
                # Ajout d'une nouvelle étagère
                wagon.append({"Longueur": item["Longueur"], "Largeur": item["Largeur"]})
                placed = True
                break

        if not placed:
            # Si la marchandise n'a pas pu être placée dans les wagons existants, on crée un nouveau wagon
            wagons.append([{"Longueur": item["Longueur"], "Largeur": item["Largeur"]}])

    return len(wagons)

# Affichage


'''
A décommenter pour afficher les résultats
ctrl + / 
lorsque vous souhaiterez tester les autres fonctions
'''
# def show_wagons_2d(wagons: list, contenair_length: float, contenair_width: float) -> None:
#     num_wagons = len(wagons)
#     cols = math.ceil(math.sqrt(num_wagons))
#     rows = math.ceil(num_wagons / cols)
    
#     fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
    
#     if rows > 1 or cols > 1:
#         axes = axes.flatten()
#     else:
#         axes = [axes]
    
#     for i, (wagon, ax) in enumerate(zip(wagons, axes)):
#         ax.set_xticks([])
#         ax.set_yticks([])
#         ax.set_xlim(0, contenair_length)
#         ax.set_ylim(0, contenair_width)
#         ax.set_aspect('equal')
#         ax.set_title(f'Wagon {i + 1}')
        
#         y_offset = 0
        
#         for shelf in wagon:
#             x_offset = 0
#             shelf_height = shelf["Largeur"]
#             for item in shelf["Items"]:
#                 color = random.choice(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
#                 ax.add_patch(plt.Rectangle((x_offset, y_offset), item["Longueur"], item["Largeur"], alpha=0.5, color=color, label=item["Désignation"]))
#                 x_offset += item["Longueur"]
            
#             y_offset += shelf_height
    
#     for j in range(i + 1, len(axes)):
#         axes[j].axis('off')
    
#     handles, labels = ax.get_legend_handles_labels()
#     fig.legend(handles, labels, loc='upper right')
    
#     plt.tight_layout()
#     plt.show()

# # Exemple d'utilisation
# details_wagons, num_wagons = nb_wagons_offline_d2(marchandises)

# show_wagons_2d(details_wagons, 11.583, 2.294)


'''
d3 = volume occupé par marchandise
d3 on peut les empiler si on veut
d3 = longueur + largeur + hauteur

On line = marchandises ne peuvent pas être triées
marchandise = premier arrivé premier affectée (pile)
Off line = trier les marchandises avant de les charger dans les conteneurs

conteneurs longueur = 11,583 mètres
conteneurs largeur = 2,294 mètres
conteneurs hauteur = 2,294 mètres

continuer avec la méthode Shelf First Fit Decreasing pour d = 3

Algorithme Shelf First Fit Decreasing :

1.Trier les marchandises par volume (largeur * longueur * hauteur) en ordre décroissant.
2.Initialiser une liste de wagon vide
3.Parcourir chaque marchandise triée    
4.Pour chaque marchandise triée, parcourir la liste des wagons existants
5.Pour chaque wagon, parcourir les couches existantes (les couches sont les différents niveaux definis par la largeur d'un objet comme fais en d2)
6.Pour chaque couche, parcourir les étagères existantes (les étagères sont dans chaque niveau de couche, elles sont côte à côte via la hauteur (profondeur), plusieurs étagères les unes a coté des autres en 3D)
7.Si la marchandise à une largeur inférieur à l'étagère, que l'addition de sa longueur à celle de l'étagère est inférieur ou égale à la longueur du wagon et que la hauteur de la marchandise est inférieur ou égale à la hauteur de l'étagère alors on l'ajoute à l'étagère
8.Si la marchandise ne rentre pas dans l'étagère on crée une nouvelle étagère en hauteur et on l'ajoute à la couche
9.Si on ne peut plus placer d'étagère dans la couche, on crée une nouvelle couche
10.Si on ne peut plus placer de couche dans le wagon, on crée un nouveau wagon
11.Retourner le nombre de wagons utilisés
'''


def nb_wagons_offline_d3(dico, wagon_longueur=11.583, wagon_largeur=2.294, wagon_hauteur=2.569):
    wagons = []  # Initialisation de la liste des wagons
    dico = sorted(dico, key=lambda x: (x["Largeur"] * x["Longueur"] * x["Hauteur"]), reverse=True)  # Tri des marchandises par volume décroissant

    for item in dico:  # Parcours des marchandises triées
        placed = False  # Initialisation de la variable pour vérifier si l'item a été placé
        for wagon in wagons:  # Parcours des wagons
            for couche in wagon:  # Parcours des couches dans un wagon
                for shelf in couche:  # Parcours des étagères dans une couche
                    if item["Largeur"] <= shelf["Largeur"] and (shelf["Longueur"] + item["Longueur"]) <= wagon_longueur and item["Hauteur"] <= shelf["Hauteur"]:
                        # Ajout de l'item à l'étagère existante
                        shelf["Longueur"] += item["Longueur"]
                        shelf["Items"].append(item)
                        placed = True
                        break
                if placed:
                    break
                # Si la marchandise ne rentre pas dans les étagères existantes, création d'une nouvelle étagère
                total_shelf_width = sum(s["Largeur"] for s in couche)
                if (total_shelf_width + item["Largeur"]) <= wagon_largeur:
                    couche.append({"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Hauteur": item["Hauteur"], "Items": [item]})
                    placed = True
                    break
            if placed:
                break
            # Si la marchandise ne rentre pas dans les couches existantes, création d'une nouvelle couche
            total_couche_height = sum(max(s["Hauteur"] for s in couche) for couche in wagon)
            if (total_couche_height + item["Hauteur"]) <= wagon_hauteur:
                wagon.append([{"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Hauteur": item["Hauteur"], "Items": [item]}])
                placed = True
                break
        if not placed:
            # Si la marchandise ne rentre pas dans les wagons existants, création d'un nouveau wagon
            wagons.append([[{"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Hauteur": item["Hauteur"], "Items": [item]}]])

    return wagons, len(wagons)




def nb_wagons_online_d3(dico, wagon_longueur=11.583, wagon_largeur=2.294, wagon_hauteur=2.569):
    wagons = []  # Initialisation de la liste des wagons

    for item in dico:  # Parcours des marchandises triées
        placed = False  # Initialisation de la variable pour vérifier si l'item a été placé
        for wagon in wagons:  # Parcours des wagons
            for couche in wagon:  # Parcours des couches dans un wagon
                for shelf in couche:  # Parcours des étagères dans une couche
                    if item["Largeur"] <= shelf["Largeur"] and (shelf["Longueur"] + item["Longueur"]) <= wagon_longueur and item["Hauteur"] <= shelf["Hauteur"]:
                        # Ajout de l'item à l'étagère existante
                        shelf["Longueur"] += item["Longueur"]
                        shelf["Items"].append(item)
                        placed = True
                        break
                if placed:
                    break
                # Si la marchandise ne rentre pas dans les étagères existantes, création d'une nouvelle étagère
                total_shelf_width = sum(s["Largeur"] for s in couche)
                if (total_shelf_width + item["Largeur"]) <= wagon_largeur:
                    couche.append({"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Hauteur": item["Hauteur"], "Items": [item]})
                    placed = True
                    break
            if placed:
                break
            # Si la marchandise ne rentre pas dans les couches existantes, création d'une nouvelle couche
            total_couche_height = sum(max(s["Hauteur"] for s in couche) for couche in wagon)
            if (total_couche_height + item["Hauteur"]) <= wagon_hauteur:
                wagon.append([{"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Hauteur": item["Hauteur"], "Items": [item]}])
                placed = True
                break
        if not placed:
            # Si la marchandise ne rentre pas dans les wagons existants, création d'un nouveau wagon
            wagons.append([[{"Longueur": item["Longueur"], "Largeur": item["Largeur"], "Hauteur": item["Hauteur"], "Items": [item]}]])

    return wagons, len(wagons)






"""Question 2"""

"""Evaluerez la complexité de votre algorithme. Un usage de la librairie time pour représenter le temps
de calcul en fonction du nombre de marchandises serait un bon début pour représenter l’évolution
du temps de calcul en fonction de la taille des données en entrée."""

def mesure_temps(fonction, *args, **kwargs):
#*args on l'utilise pour une liste d'arguments non nommés
#**kwargs permet de passer un nombre variable d'arguments nommés à une fonction (a=1, b=2, c=3) ce qui va donc nous permettre d'envoyer notre dictionnaire d'objets
#https://deusyss.developpez.com/tutoriels/Python/args_kwargs/

    # Mesure le temps d'une seule exécution pourra nous servir plus tard
    #on reprend ce qu'on a fait en IA pour calculer le temps d'execution de notre fonction
    start = time.time()
    fonction(*args, **kwargs)
    end = time.time()
    temps_single = end - start

    # or cette mesure peut ne pas être très précise car le temps d'exécution est très court
    # on va donc effectuer 1000 répétitions pour obtenir un temps d'exécution plus significatif
    # a mettre en comment pour les fonctions plus complexes
    repetitions = 10000
    start = time.time()
    for _ in range(repetitions):
        fonction(*args, **kwargs)
    end = time.time()
    temps_multiple = (end - start) / repetitions

    return temps_single, temps_multiple

# Mesure du temps pour chaque fonction
temps_d1_single, temps_d1_multiple = mesure_temps(nb_wagons_offline_d1, marchandises)
print(f"Temps d'exécution pour nb_wagons_offline_d1: {temps_d1_single:.6f}, {temps_d1_multiple:.6f} secondes")

temps_d1_o_single, temps_d1_o_multiple = mesure_temps(nb_wagons_online_d1, marchandises)
print(f"Temps d'exécution pour nb_wagons_online_d1: {temps_d1_o_single:.6f}, {temps_d1_o_multiple:.6f} secondes")

temps_d2_single, temps_d2_multiple = mesure_temps(nb_wagons_offline_d2, marchandises)
print(f"Temps d'exécution pour nb_wagons_offline_d2: {temps_d2_single:.6f}, {temps_d2_multiple:.6f} secondes")

temps_d2_o_single, temps_d2_o_multiple = mesure_temps(nb_wagons_online_d2, marchandises)
print(f"Temps d'exécution pour nb_wagons_online_d2: {temps_d2_o_single:.6f}, {temps_d2_o_multiple:.6f} secondes")

time_d3_offline, result_d3_offline = mesure_temps(nb_wagons_offline_d3, marchandises)
print(f"Temps d'exécution pour nb_wagons_offline_d3: {time_d3_offline:.6f}, {result_d3_offline:.6f} secondes")

temps_d3_o_single, temps_d3_o_multiple = mesure_temps(nb_wagons_online_d3, marchandises)
print(f"Temps d'exécution pour nb_wagons_online_d3: {temps_d3_o_single:.6f}, {temps_d3_o_multiple:.6f} secondes \n\n")


"""Question 3"""

"""(Difficile) Pour aller plus loin, vous pourriez essayer d’obtenir des informations sur sa complexité
(complexité au pire, borne supérieure ...)"""

wagon_offline_d1 = nb_wagons_offline_d1(marchandises)
wagon_online_d1, wagon_detail = nb_wagons_online_d1(marchandises)
print(f"Le nombre de wagons pour d = 1 en offline : {wagon_offline_d1}")
print(f"Le nombre de wagons pour d = 1 en online : {wagon_online_d1}\n")
print(f"Voici le contenu des wagons pour d = 1 en oline : {wagon_detail}\n\n")

wagon_offline_d2, wagon_detail = nb_wagons_offline_d2(marchandises)
wagon_online_d2 = nb_wagons_online_d2(marchandises)
print(f"Le nombre de wagons pour d = 2 en offline : {wagon_detail}")
print(f"Le nombre de wagons pour d = 2 en online : {wagon_online_d2}\n")
print(f"Voici le contenu des wagons pour d = 2 en offline : {wagon_offline_d2}\n\n")


details_wagons, num_wagons = nb_wagons_offline_d3(marchandises)
print(f"Le nombre de wagons pour d = 3 en offline : {num_wagons}")
#print(f"Voici le contenu des wagons pour d = 3 en offline : {details_wagons}")
details_wagons, num_wagons = nb_wagons_online_d3(marchandises)
print(f"Le nombre de wagons pour d = 3 en online : {num_wagons}")
#print(f"Voici le contenu des wagons pour d = 3 en offline : {details_wagons}")
