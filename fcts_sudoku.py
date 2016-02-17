#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Programme Sudoku
fait le 11/10/2014
Python 2.7.6 
"""

import numpy as np
from random import randrange
#import time

# ============================================================================
# Classes
# ============================================================================
class Sudoku():
    """
    Permet de définir et résoudre un sudoku
    """

    def __init__(self, data):
        """
        initialise le sudoku
        """
        self.tableau = data # tableau initiale - celui à résoudre
        self.solution = np.zeros((9, 9)) # initialisation - tableau solution
        self.iteration = 0 # nb d'itérations avant résultat final

    def ligne(self, i):
        """
        liste des nb dans une ligne
        """
        return self.solution[i, :]

    def colonne(self, j):
        """
        liste des nb dans une colonne
        """
        return self.solution[:, j]

    def pos_carre(self, i, j):
        """
        retourne la position d'un sous tableau sudoku
        """
        return 3*(i//3), 3*(j//3)

    def carre(self, i, j):
        """
        retourne l'ensemble de nb d'un sous tableau
        """
        pos_i, pos_j = self.pos_carre(i, j)
        sous_tableau = self.solution[pos_i:pos_i+3, pos_j:pos_j+3]
        return sous_tableau

    def presence_valeur(self, i, j, val):
        """
        test booleen pour savoir si un chiffre est déjà dans le tableau
        """
        return (val in self.ligne(i)) \
                or (val in self.colonne(j)) \
                or (val in self.carre(i, j))

    def case_vide(self, i, j):
        """
        test pour savoir si la case est rempli ou non
        """
        return self.tableau[i, j] == 0

    def avance(self, i, j, val):
        """
        détermine les indices de la case suivante pour la recherche
        """
        # on avance
        j = j+1
        val = 1
        if j > 9:
            i = i+1
            j = 1
        return i, j, val

    def recule(self, i, j, val):
        """
        détermine les indices de la case précédente pour la recherche
        """
        # on recule
        j = j-1
        if j < 0:
            j = 8
            i = i-1
        # on efface la valeur precedente
        # puis on teste la valeur suivante
        val = self.solution[i, j]+1
        if self.case_vide(i, j):
            self.solution[i, j] = 0
        else:
            i, j, val = self.recule(i, j, val)
        return i, j, val


    def deplacement(self, i, j, val):
        """
        gère le suivi de la case de recherche
        """
        if val < 10:
#            print "en avant"
            return self.avance(i, j, val)
        else:
#            print "en arrière"
            return self.recule(i, j, val)

    def solvee(self):
        self.solve()
        lfin=list()
        while 9>len(lfin):
                k=randrange(1,10)
                if k not in lfin:
                        lfin.append(k)
                        
        # on parcours tout le self.tableau
        i = 0
        while i < 9:
                j = 0
                while j < 9:
                        val=self.solution[i, j]
                        for l, elt in enumerate(lfin):
                                if l+1 == int(val):
                                            self.solution[i, j] = elt
                                #print(i,j,l," ",elt," ",val)
                        j+=1
                i+=1
        #print self.solution

    
    def verification(self):
        
        self.solution = np.copy(self.tableau)
        i = 0
        d=True
        while i < 9:
            j = 0
            while j < 9:
                val=self.solution[i, j]
                a=list(self.ligne(i))
                b=list(self.colonne(j))
                c=list(self.carre(i, j))
                
                s=list(c[0])   
                t=list(c[1]) 
                u=list(c[2]) 
                w= s+t+u
                if not (a.count(val)<2 and b.count(val)<2 and w.count(val)<2 or str(val)=="0.0"):
                    d=False
                j+=1
            i += 1
        return d
                


    def solve(self):
        """
        resolution récursive du sudoku
        ne gère pas les sudoku sans solution
        """
        self.solution = np.copy(self.tableau)
        # on parcours tout le self.tableau
        i = 0
        while i < 9:
            j = 0
            val = 1
            while j < 9:
                # on teste toutes les valeurs
                if self.case_vide(i, j) and val < 10:
                    if self.presence_valeur(i, j, val):
                        val = val+1
                    else:
                        self.solution[i, j] = val
                        self.iteration = self.iteration + 1
#                        affiche_tab(self.solution)
#                        time.sleep(0.1)
                        i, j, val = self.deplacement(i, j, val)
                else:
                    i, j, val = self.deplacement(i, j, val)
            i = i + 1
