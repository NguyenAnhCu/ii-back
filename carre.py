from math import *


def ligne(c):
    a = ceil(c / 3)
    return a


def colonne(c):
    if (c % 3) == 0:
        return 3
    else:
        return c % 3


# paramètre de l'image suivante
# k,c = cardinalite,u,d = position ,o,r =rang
def carre():
    liste = [(1, 1, 1)]
    r = 2
    while r <= 8:
        # calcul cardinalite
        k = ligne(r)
        # calcul position
        u = colonne(r)
        liste.append((r, k, u))
        # calcul rang
        r = r + 1

    print("rang, card, pos", liste)


carre()
