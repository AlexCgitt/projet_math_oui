"""CAVARO.A & LAMOULEN.L"""
import time
'''

--------------------------------------
Partie 1:


Nos données sont les suivantes :
    - les objets ont une masse et une utilité
    - la charge total du sac ne doit pas dépasser la constante C
    - il faut optimisé le plus possible le poid avec l'utilité 
    (respecter le poid C et avoir le plus de chose utile dans notre sac)
    - on associe à chaque objet o d'une liste L à une variable binaire : 1 si objet dans sac, 0 sinon
  
------------------------
Enoncé

Un cycliste à un sac à dos, la masse total des objets qu'il peut transportée dans son sac à dos est une constante C


------------------------------------
'''
# Dictionnaire des objets avec le nom de l'objet, sa masse et son utilité
objects = {
    "Pompe": {"Masse": 0.2, "Utilité": 1.5},
    "Démonte-pneus": {"Masse": 0.1, "Utilité": 1.5},
    "Gourde": {"Masse": 1, "Utilité": 2},
    "Chambre à air": {"Masse": 0.2, "Utilité": 0.5},
    "Clé de 15": {"Masse": 0.3, "Utilité": 1},
    "Multi-tool": {"Masse": 0.2, "Utilité": 1.7},
    "Pince multiprise": {"Masse": 0.4, "Utilité": 0.8},
    "Couteau suisse": {"Masse": 0.2, "Utilité": 1.5},
    "Compresses": {"Masse": 0.1, "Utilité": 0.4},
    "Désinfectant": {"Masse": 0.2, "Utilité": 0.6},
    "Veste de pluie": {"Masse": 0.4, "Utilité": 1},
    "Pantalon de pluie": {"Masse": 0.4, "Utilité": 0.75},
    "Crème solaire": {"Masse": 0.4, "Utilité": 1.75},
    "Carte IGN": {"Masse": 0.1, "Utilité": 0.2},
    "Batterie Portable": {"Masse": 0.5, "Utilité": 0.4},
    "Téléphone mobile": {"Masse": 0.4, "Utilité": 2},
    "Lampes": {"Masse": 0.3, "Utilité": 1.8},
    "Arrache Manivelle": {"Masse": 0.4, "Utilité": 0},
    "Bouchon valve chromé bleu": {"Masse": 0.01, "Utilité": 0.1},
    "Maillon rapide": {"Masse": 0.05, "Utilité": 1.4},
    "Barre de céréales": {"Masse": 0.4, "Utilité": 0.8},
    "Fruits": {"Masse": 0.6, "Utilité": 1.3},
    "Rustines": {"Masse": 0.05, "Utilité": 1.5}
}

objets_2 = [
    {"Nom": "Gourde", "Masse": 1, "Utilité": 2},
    {"Nom": "Fruits", "Masse": 0.6, "Utilité": 1.3},
    {"Nom": "Batterie Portable", "Masse": 0.5, "Utilité": 0.4},
    {"Nom": "Pince multiprise", "Masse": 0.4, "Utilité": 0.8},
    {"Nom": "Veste de pluie", "Masse": 0.4, "Utilité": 1},
    {"Nom": "Pantalon de pluie", "Masse": 0.4, "Utilité": 0.75},
    {"Nom": "Crème solaire", "Masse": 0.4, "Utilité": 1.75},
    {"Nom": "Téléphone mobile", "Masse": 0.4, "Utilité": 2},
    {"Nom": "Arrache Manivelle", "Masse": 0.4, "Utilité": 0},
    {"Nom": "Barre de céréales", "Masse": 0.4, "Utilité": 0.8},
    {"Nom": "Clé de 15", "Masse": 0.3, "Utilité": 1},
    {"Nom": "Lampes", "Masse": 0.3, "Utilité": 1.8},
    {"Nom": "Pompe", "Masse": 0.2, "Utilité": 1.5},
    {"Nom": "Chambre à air", "Masse": 0.2, "Utilité": 0.5},
    {"Nom": "Multi-tool", "Masse": 0.2, "Utilité": 1.7},
    {"Nom": "Couteau suisse", "Masse": 0.2, "Utilité": 1.5},
    {"Nom": "Désinfectant", "Masse": 0.2, "Utilité": 0.6},
    {"Nom": "Démonte-pneus", "Masse": 0.1, "Utilité": 1.5},
    {"Nom": "Compresses", "Masse": 0.1, "Utilité": 0.4},
    {"Nom": "Carte IGN", "Masse": 0.1, "Utilité": 0.2},
    {"Nom": "Maillon rapide", "Masse": 0.05, "Utilité": 1.4},
    {"Nom": "Rustines", "Masse": 0.05, "Utilité": 1.5},
    {"Nom": "Bouchon valve chromé bleu", "Masse": 0.01, "Utilité": 0.1}
]

'''
-----------------------------------------
#question 1

On fixe N le nombre d’objets dans le sac à dos.
sans tenir compte de la contrainte de charge max

combien de sac à dos contenant N objets peut-on réaliser ?

calcule du nombre de sac à dos pour N  ∈ {1, 2, 10, 23}
'''
#  On crée une fonction qui permet de calculer le nombre de sac à dos pour N objets
#  On prend 2 puissance N car pour chaque objet on a 2 choix : le mettre dans le sac ou ne pas le mettre


def puissancede2(n):
    return 2**n

print("\n\n-------------------QUESTION 1:----------------------\n\n")
# Ce print sert à tester la fonction
print("le nombre de sac à dos pour 23 objets est de : ", puissancede2(23))  # 8388608 sacs à dos avec 23 objets
print("le nombre de sac à dos pour 10 objets est de : ", puissancede2(10))  # 1024 sacs à dos avec 10 objets
print("le nombre de sac à dos pour 2 objets est de : ", puissancede2(2))  # 4 sacs à dos avec 2 objets
print("le nombre de sac à dos pour 1 objet est de : ", puissancede2(1))  # 2 sacs à dos avec 1 objet


'''
-----------------------------------------
#question 2

cb d'organisation de sac à dos peut-on former au total ?
on ne prend pas en compte poid max
Donc il nous suffit juste de prendre le N max pour savoir le nombre total de sac à dos possible
'''

print("\n\n-------------------QUESTION 2:----------------------\n\n")
print("\nle nombre total de sac à dos possible est de : ", puissancede2(23), "sacs à dos possibles")



'''
-------------------------------------------------------
#question 3

Résoudre le problème à la main pour C = 0.6
Donc respecter le poid C et avoir le plus de chose utile dans notre sac
En resolvant à la main on a trouvé que l'optimisation qui maximise 
l'utilité en respectant le poid C est la liste d'objet suivante :
Maillon rapide + Rustines + Démonte-pneus + Pompe ou couteau suisse + Multi-outils
poid total de notre sac = 0.05 + 0.05 + 0.1 + 0.2 + 0.2 = 0.6
utilité total de notre sac =  1.4 + 1.5 + 1.5 + 1.5 + 1.7 = 7.6
pour réaliser cette opération nous avons fonctionner par comparaison.
On a éliminé les objets ayant une masse supérieur à C
puis on a comparé les objets restants pour voir 
si on pouvait les remplacer par des objets ayant une masse inférieur à C.
En fonctionnant sous forme de pile 
c'est à dire en commençant par les objets les plus lourds, on a pu trouver la solution optimale.
'''


'''
-------------------------------------------------------
#question 4 5 6

Ecriture d'un algorithme répondant à ce qui à été fait en question 3.
Cet algorithme doit permettre de trouver la solution optimale qui maximise l'utilité en respectant le poid C (ici 0.6)

1. On trie les objets par ordre décroissant de ratio utilité/masse (utile pour les objets de faible masse cela va permettre de les mettre dans le sac en priorité)
2. On va ensuite créer une liste vide (sac) qui va contenir les objets que l'on va mettre dans le sac.
3. On va initialiser la masse total du sac (poids_total) à 0 pour suivre l'évolution de la masse total du sac.
4. On parcourt les objets triés et pour chaque objet :
    si l'ajout de l'objet ne dépasse pas le poids C (poids_total + objet["Masse"] <= C) alors on ajoute l'objet dans le sac et on ajoute sa masse à la masse total du sac
5. une fois que l'on a parcouru tous les objets ou atteint le poid C on retourne le sac et on arrête l'algorithme

'''
print("\n\n-------------------QUESTION 4 5 6:----------------------\n\n")
#Ecriture de l'algorithme en python
def maximiser_utilite_initial(objets, C):

    objets_tries = sorted(objets.items(), key=lambda x: x[1]["Utilité"]/x[1]["Masse"], reverse=True) 
# la ligne ci-dessus va nous permettre de trier le dictionnaire objets en fonction du rapport entre l'utilité et la masse de chaque objet (ratio). objets.item() va nous permmettre de retourner des paire clé valeurs (un tuple) ex : ('Pompe', {'Masse': 0.2, 'Utilité': 1.5})
#key=lambda x: x[1]["Utilité"]/x[1]["Masse"] fonction lambda qui prend donc en entré notre tuple et qui va nous retourner le ratio de chaque objet. x[1] pour accéder au dictionnaire de chaque objet et ["Utilité"] ["Masse"] pour accéder à l'utilité et la masse de chaque objet.
#on aurait pris x[0] on aurait trié les noms donc bof
#reverse=True pour trier par ordre décroissant


    sac = [] #liste qui va contenir les objets que l'on va mettre dans le sac
    poids_total = 0 #va nous permettre d'obtenir la masse total du sac
    utilité_total = 0 #va nous permettre d'obtenir l'utilité total du sac

#pas forcement besoin d'expliquer la boucle for car c'est plutôt explicite
    for objet in objets_tries:
        if poids_total + objet[1]["Masse"] <= C:
            sac.append(objet)
            poids_total += objet[1]["Masse"]
            utilité_total += objet[1]["Utilité"]
    
    return sac, poids_total, utilité_total

#Test de l'algorithme
sac, _, _ = maximiser_utilite_initial(objects, 0.6)
print("\n\nVoici donc une liste des objets maximisant l'utilité en respectant le poid C",sac) #On obtient la liste d'objet suivante : 'Rustines', 'Maillon rapide', 'Démonte-pneus', 'Bouchon valve chromé bleu', 'Multi-tool', 'Compresses',


_, poids_total, _= maximiser_utilite_initial(objects, 0.6)#On obtient un poid total de 0.6
print("\nLa masse total de notre sac est de", poids_total)

_, _, utilité_total = maximiser_utilite_initial(objects, 0.6)#On obtient une utilité total de 6.6000000000000005
print("\nL'utilité total de notre sac est de", utilité_total)

# Cette méthode est la plus simple qui nous est venue à l'esprit pour résoudre ce problème.

'''
On va maintenant essayer de determiner le temps de calcul de notre algorithme en fonction du nombre d'opérations à effectuer.
Pour cela on va utiliser la librairie time qui va nous permettre de mesurer le temps de calcul de notre algorithme.
On va faire varier n pour observer comment le  temps de réponse de l'algorithme change en fonction du nombre d'opérations à effectuer.
On va noter T le temps qu'il va nous falloir pour effectuuer 1 opération.


Le temps d'execution de notre fonction étant très court on va devoir effectuer un grand nombre de répétitions pour obtenir un temps d'execution significatif.
'''
#time a été importé en début de code


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

# Utilisation
temps_single, temps_multiple = mesure_temps(maximiser_utilite_initial, objects, 0.6)
print(f"\nTemps pour une seule exécution: {temps_single} secondes")
print(f"Temps moyen avec répétition exécutions: {temps_multiple} secondes\n\n")


'''
-------------------------------------------------------
#question 7 8 9

Rédaction d'un algorithme exact pour la résolution du problème du sac à dos
possibilité d'utiliser la méthode de la force brute pour résoudre ce problème
possibilité d'utiliser la méthode de la programmation dynamique pour résoudre ce problème
possibilité d'utiliser la méthode de la programmation linéaire pour résoudre ce problème (méthode du simplexe, méthode cplex, méthode gurobi, méthode glpk, méthode scipy)
possibilité d'utiliser la méthode de la programmation linéaire en nombre entier pour résoudre ce problème (Branch and Bound, Branch and Cut)

On va pouvoir abordé plusieurs solutions mais commençons par la plus simple : la force brute

- objectif force brute : 
    On va parcourir tous les objets possibles et on va les mettre dans le sac ou non. (représentation bianaire 0 ou 1)
    Notre nombre de possibilité va être de 2^N
    On va tester toutes les combinaisons possibles et on va garder la meilleure.
    Notre complexité va être O(2^N) ce qui est très long.
    On va donc utiliser cette méthode pour un petit nombre d'objets.

    méthode récursive

    Algorithme A_force_brute(objets, C, meilleur_sac=[]):
    1. Initialiser la variable poids_total à 0
    2. Si liste des objets est non vide alors :
    3.     Pour chaque objet dans objets :
    4.         Si objet[1]["Masse"] <= C soit le poids_total alors :
    5.             Ajouter l'objet à list_meilleur_sac et augmenter poids_total par objet["Masse"]
    6.             Rappeler recursivement A_force_brute(objets - objet, C - poids_total)
    7.         Sinon, ignorer l'objet et rappeler A_force_brute(objets - objet, C)
    8. Comparer les utilités des 2 listes de sac et garder la meilleure
    9. Retourner la liste de sac avec la meilleure utilité

    code : 
        def utilite(sac):
        return sum(objet[1]["Utilité"] for objet in sac)

        def force_brute(objets, c, sac=[], meilleur_sac=[]):
            if not objets:
                if utilite(sac) > utilite(meilleur_sac):
                    meilleur_sac = list(sac)
            else:
                objet, *reste = objets #on prend le premier objet de la liste et on met le reste dans reste (regardé doc python unpacking avec lien plus haut)
                if objet[1]["Masse"] <= c:
                    sac.append(objet)
                    meilleur_sac = force_brute(reste, c - objet[1]["Masse"], sac, meilleur_sac)
                    sac.pop() #permet de retirer le dernier élément de la liste
                meilleur_sac = force_brute(reste, c, sac, meilleur_sac)
            return meilleur_sac

    Après avoir rencontré des soucis, nous avons décidé de changer de méthode pour résoudre ce problème.
    Basculons sur une méthode itérative du force brute pour résoudre ce problème. l'objectif du force brute va rester le même.

    Algorithme A pour la force brute itératif :
        1. Définir le nombre total d'objets (nbre) dans la liste
        2. Calculer le nombre total de combinaisons possibles (possibility) : 2^nbre
        3. Initialiser la meilleure combinaison à une liste vide
        4. Pour chaque combinaison possible de 0 à possibility :
        5.     Convertir le numéro d'itération actuel en binaire et enlever les 2 premiers caractères (0b) pour obtenir une chaine de caractère
        6.     Si la longueur de la chaine est inférieure au nombre d'objets, ajouter des 0 devant pour avoir une chaine de la bonne longueur
        7.     Initialiser une liste vide qui contiendra la combinaison d'objets actuelle
        8.     Pour chaque caractère de la chaine binaire :
        9.         Si le caractère est un 1, ajouter l'objet correspondant à la position actuelle dans la liste d'objets
        10.    Comparer la combinaison actuelle à la meilleure combinaison trouvée jusqu'à présent
        11.    Si la nouvelle combinaison a une meilleure utilité et ne dépasse pas la capacité maximale, la sauvegarder comme la meilleure combinaison.
        12. Retourner la meilleure combinaison

'''

print("\n\n-------------------QUESTION 7,8,9:----------------------\n\n")

#fonction qui calcule l'utilité totale d'une sélection d'objets, dans notre cas une liste.
def utilite_totale(selection):
    utilite = 0 #On initialise la variable utilité à 0 qui accumulera l'utilité totale des objets
    for objet in selection:
        utilite += objet["Utilité"]#pour chque objet dans notre selection, on va ajouter la valeur de l'utilité de l'objet à notre variable utilité
    return utilite

#fonction qui calcule la masse totale d'une sélection d'objets, dans notre cas, une liste.
def masse_totale(selection):
    masse = 0#On initialise la variable masse à 0 qui accumulera la masse totale des objets
    for objet in selection:
        masse += objet["Masse"]#pour chaque objet dans notre selection, on va ajouter la valeur de la masse de l'objet à notre variable masse
    return masse

#foncion itérative de force brute
def force_brute(objets, c):
    nbre = len(objets) #nbre est le nombre total d'objets dans notre liste
    possibility = 2 ** nbre #on la montré dans la question 1 2**n , c'est le nombre de combinaison possible. 
    meilleure_combinaison = [] #est initialisée comme une liste vide qui contiendra la meilleure combinaison d'objets trouvée

    for x in range(possibility): # on va parcourir toutes les combinaisons possibles de 0 à possibility(2^nbre)
        chaine = bin(x)[2:] #on convertit x (le numéro d'itération actuel) en binaire et on enlève les 2 premiers caractères (0b) pour obtenir une chaine de caractère
        long = len(chaine) # va calculer la longueur de la chaine 
        if long < nbre:
            chaine = (nbre - long) * '0' + chaine # Si la longueur de la chaine est inférieure au nombre d'objets, on ajoute des 0 devant pour avoir une chaine de la bonne longueur

        combinaison = []#initialise une liste vide qui contiendra la combinaison d'objets actuelle
        #chaque suite binaire va représenter une combinaison d'objets
        #on parcours donc chaque caractère de la chaine binaire
        #on verifie si le caractère est un 1, si c'est le cas on ajoute l'objet correspondant à la position actuelle dans la liste d'objets
        for i in range(nbre):
            if chaine[i] == '1':
                combinaison.append(objets[i])
        #on compare ensuite la combinaison actuelle à la meilleure combinaison trouvée jusqu'à présent
        if utilite_totale(combinaison) > utilite_totale(meilleure_combinaison):
            #si la combinaison actuelle est meilleure, on la remplace par la meilleure combinaison
            if masse_totale(combinaison) <= (c+0.0000000000000001): #on ajoute une petite marge d'erreur pour éviter les erreurs d'arrondi car en python les nombres flottants ne sont pas toujours exacts
                meilleure_combinaison = combinaison

    return meilleure_combinaison


start_exact = time.time()
meilleure_combinaison = force_brute(objets_2, 0.6)
end_exact = time.time()
noms_objets = [objet["Nom"] for objet in meilleure_combinaison]
utilite_max = utilite_totale(meilleure_combinaison)
new_weight = masse_totale(meilleure_combinaison)

print(f"\n\nMeilleure combinaison d'objets: {noms_objets}")
print(f"Utilité totale: {utilite_max}")
print(f"Poids total: {new_weight} \n")

temps_A_exact = end_exact - start_exact

print(f"Temps d'exécution de l'algorithme A: {temps_A_exact} secondes\n\n")


# temps_single = mesure_temps(force_brute, objets_2, 0.6)
# print(f"Temps pour une seule exécution: {temps_single} secondes")
#print(f"Temps moyen avec répétition exécutions: {temps_multiple} secondes\n\n")
# environ 15.3 seconde varie en fonction des pc 33 seconde pour lea



'''
-------------------------------------------------------
#question 10 11 12
On va reprendre ce qui a été fait en question 4 5 6
Suite à des problèmes rencontré avec l'ancien dictionnaire d'objet nous avons décidé d'en creer un nouveau
On est en présence d'un algorithme approché de type glouton
Une approche différente a été réalisée pour calculer le temps d'exécution de notre algorithme
On étudie notre algorithme en choisissant différentes valeurs de C, pour ainsi observer comment le temps de réponse de l'algorithme change.

'''

print("\n\n-------------------QUESTION 10 11 12:----------------------\n\n")

t = 10 ** -6  # On fixe une constante d'exécution égale à 1 microseconde pour chaque opération


def maximiser_utilite(objets, c, t):

    temps_final = 0
    objets.sort(key=lambda x: x["Utilité"]/x["Masse"], reverse=True)
    temps_final += t
    sac = []
    temps_final += t
    poids_total = 0
    temps_final += t
    utilite_total = 0  # va nous permettre d'obtenir l'utilité total du sac
    temps_final += t

    for objet in objets:
        temps_final += t
        if poids_total + objet["Masse"] <= c:
            temps_final += 2*t
            sac.append(objet)
            temps_final += t
            poids_total += objet["Masse"]
            temps_final += 2*t
            utilite_total += objet["Utilité"]
            temps_final += 2*t

    return sac, poids_total, utilite_total, temps_final


""" Question 10 11 12 13 """


def algo_naif(c, objets_2, t):
    temps_final = 0
    objets_2.sort(key=lambda x: x["Utilité"], reverse=True)
    temps_final += t
    sac = []
    temps_final += t
    poids_tot = 0
    temps_final += t
    utilite_tot = 0
    temps_final += t

    for i in objets_2:
        temps_final += t
        if i["Masse"] + poids_tot <= c:
            temps_final += 2 * t
            sac.append(i)
            temps_final += t
            poids_tot += i["Masse"]
            temps_final += 2 * t
            utilite_tot += i["Utilité"]
            temps_final += 2 * t

    return sac, poids_tot, utilite_tot, temps_final


diff_capa = [0.6, 2, 3, 4, 5]
for k in objets_2:
    k["Masse"] = int(k["Masse"] * 100)  # On convertit les masses en entier
    k["Utilité"] = int(k["Utilité"] * 100)  # On convertit les utilités en entier

for i in diff_capa:
    c = int(i * 100)
    sac_glout, poids_tot_glout, util_tot_glout, temps_glout = maximiser_utilite(objets_2, c, t)
    sac_naif, poids_tot_naif, util_tot_naif, temps_naif = algo_naif(c, objets_2, t)


    print(f"Algo glouton => Capacité : {c/100}, Utilité : {util_tot_glout/100}, Temps : {temps_glout}")
    print(f"Algo naïf => Capacité : {c / 100}, Utilité : {util_tot_naif / 100}, Temps : {temps_naif}\n")


    # temps_single, temps_multiple = mesure_temps(maximiser_utilite, objets_2, c)
    # print(f"\nTemps pour une seule exécution: {temps_single} secondes")
    # print(f"Temps moyen avec répétition exécutions: {temps_multiple} secondes\n")

'''
Question 13

l'algorithme exact examine toutes les combinaisons possible pour trouver la solution optimale.
Il garantit de trouver la solution optimale mais il est très coûteux en temps de calcul surtout pour un grand nombre d'objets.
Le temps d'exécution de l'algorithme exact augmente exponentiellement avec le nombre d'objets,
ce qui le rend impraticable pour de grands ensembles d'objets.

L'algorithme approché tente quant à lui de trouver une solution optimale en un temps raisonnable.
Il ne garantit pas de trouver la solution optimale mais il donne une bonne approximation de la solution optimale.
Il est beacoup plus rapide que l'algorithme exact mais il peut donner des résultats moins bons.

'''