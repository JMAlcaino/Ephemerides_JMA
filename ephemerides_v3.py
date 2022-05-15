# Programme pour tester PyEphem
# Module de calculs astronomiques

"""
* Liste des variables utilisées :
- date → calcul de date pour datetime.now et pour la date choisie
- date_format → str avec le bon format pour calculer éphémérides
- choix_date → choix entre now et date perso
- j, m, a, h, mn et s → variables pour définir la date choisie personnellement

* Améliorations :
- heures locales ou UTC
- heures selon le fuseau horaire
- tests de validité des dates (jours et mois)
- test années bissextiles
- noms des planètes en français
- nom des constellations en francais
- formater l'affichage des résultats.'
"""
import ephem  # Librairie de calculs astro
from datetime import datetime  # Librairie date et heure


# Mise en place des fonctions
def generique():  # À finaliser avec autres progs
    print()
    print('       --- ÉPHÉMÉRIDES ---\n')
    print()
    print('Petit programme pour calculer les\n')
    print('éphémérides du Système Solaire.')
    print()


def calcul_now():  # Date et heure actuelle système + mise en format pour ephem
    date_now = datetime.now()
    date_format_now = date_now.strftime('%Y/%m/%d %H:%M:%S')
    print()
    print('Date et heure actuelle pour le calcul : ', date_format_now)
    date_format = date_format_now
    return date_format


def date_perso():  # Choix de la date de calcul
    print()
    print('Vous allez entrer la date de votre choix')
    j = int(input('Jour ?'))
    ms = int(input('Mois ?'))
    a = int(input('Année ?'))    
    h = int(input('Heure ?'))
    mn = int(input('Minutes ?'))
    s = int(input('Secondes ?'))
    date = datetime(a, ms, j, h, mn, s)
    date_format_choix = date.strftime('%Y/%m/%d %H:%M:%S')
    print('Date et heure choisies pour le calcul ', date_format_choix)
    date_format = date_format_choix
    return date_format


def planete():  # Fonction de calcul pour une seule planète
    
def systemeSolaire():   #  Calcul pour tout le Systeme Solaire
      
      
# Principal

generique()  # Appel fonction affichage générique.

# Choix de la date pour le calcul
print(' - Entrez [1] pour un calcul maintenant\n - Entrez [2] pour une date et heure de votre choix')
choix_date = int(input('Votre choix ?'))  # À améliorer avec un try/except si erreur d'entrée
if choix_date == 1:
    date_calcul = calcul_now()
else:
    date_calcul = date_perso()

# Choix du calcul (planète/Système Solaire)
print()
print(' - Entrez [1] pour le calcul pour toutes les planètes\n - Entrez [2] pour choisir une planète ')
choix_calcul=int(input('Votre choix ?'))
if choix_calcul==1:
    resultat_syssol=systemeSolaire(date_calcul)  # saute à la fonction systemeSolaire(), module de calcul global utilisant la date choisie
else:
    resultat_planete=planete(date_calcul, planete) # saute à la fonction planete(), module de calcul pour une seule planete
    
