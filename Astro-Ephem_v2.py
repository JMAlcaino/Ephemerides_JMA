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
    date = datetime.now()
    date_format = date.strftime('%Y/%m/%d %H:%M:%S')
    print()
    print('Date et heure actuelle pour le calcul : ', date_format)
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
    date_format = date.strftime('%Y/%m/%d %H:%M:%S')
    print('Date et heure choisies pour le calcul ', date_format)
    return date_format


# Principal

generique()  # Appel fonction affichage générique.

print('Choisissez pour un calcul maintenant entrez [1] ou à une date de votre choix entrez [2].')
choix_date = int(input('Votre choix ?'))  # À améliorer avec un try/except si erreur d'entrée
if choix_date == 1:
    date_format = calcul_now()
else:
    date_format = date_perso()

# essai d'affichage des calculs

m = ephem.Mars()
m.compute(date_format)
print(m.ra, m.dec)
print(ephem.constellation(m))

"""
Améliorations
- heures locales ou UTC
- heures selon le fuseau horaire
- tests de validité des dates (jours et mois)
- test années bissextiles
"""
