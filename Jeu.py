#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Résoud des sudokus - interface
Python 2.7.6
"""

from fcts_sudoku import Sudoku

#from tkinter import *   ## notice here too
import numpy as np
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randrange

# ============================================================================
# Classes
# ============================================================================
class Interface():


    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if text in '123456789' and int(index) < 1:
            return True
        else:
            return False    
    """
    Définit l'interface du jeu sudoku
    """
    def info1(self):
        messagebox.showinfo("Information", "Mini-projet réalisé par le\nGroupe:B1\nNiveau d'étude: Master1 Informatique\nAnnée d'étude: 2014-2015")

    def info2(self):
        messagebox.showinfo("Information", "Règles du jeu:\n\n   Remplir la grille de sorte que chaque Ligne,  Colonne  et  Région possède tous les chiffres de 1 à 9")

    def fNouveau(self):
        """
        on reinitialise le tableau d'entrées (Entry)
        """
        self.fcreation_entree()
#        print "azul"
        for i in range(9):
             for j in range(9):
                  self.entree[i][j].set("")
        return



    def fQuitter(self):
        """
        quitter l'application
        """
       
        if tkinter.messagebox.askokcancel("Quitter", "Voulez vous quitter la partie ?"):
            self.fenetre.destroy()
        return


    def fResoudre(self):
        """
        résoud le sudoku et affiche la solution
        ne gère pas les sudoku sans solution
        """
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                self.fResoudre
                val=self.entree[i][j].get()
                if isValid(val):
                    val=int(val)
                else:
                    val=0
                tableau[i,j]=val
        # on resoud le sudoku
        mSudok = Sudoku(tableau)
        if mSudok.verification():
            mSudok.solve()
            for i in range(9):
                for j in range(9):
                    self.entree[i][j].set( str(int(mSudok.solution[i, j])))
        else:
            tkinter.messagebox.showerror("Erreur", "Une ou plusieur valeurs dupliquées")
            
        # on affiche la solution
        
        return
        
        # on affiche la solution
        for i in range(9):
            for j in range(9):
                self.entree[i][j].set( str(int(mSudok.solution[i, j])))
        return

    #Généré une grille facile
    def facile(self):
        """
        résoud le sudoku et affiche la solution
        ne gère pas les sudoku sans solution
        """
        self.fcreation_entree()
        self.fNouveau()
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                self.facile
                val=self.entree[i][j].get()
                if isValid(val):
                    val=int(val)
                else:
                    val=0
                tableau[i,j]=val
        # on resoud le sudoku
        mSudok = Sudoku(tableau)
        mSudok.solvee()
        
        # affiche quelque nombre pour le niveau
        f=0
        s=list()
        while f<48:
            i=randrange(9)
            j=randrange(9)
        #    print "i = ",i, ", j = ",j
            if (i,j) not in s:
                    self.entree[i][j].set( str(int(mSudok.solution[i, j])))
                    tkinter.Entry(self.fenetre, textvariable=self.entree[i][j], width=2, font="Arial 30",state ='disabled',justify='center', validate='key', validatecommand=self.vcmd).grid(column=i, row=j)
                    f +=1
                    s.append((i,j))
        return

    def moyen(self):
        """
        résoud le sudoku et affiche la solution
        ps: ne gère pas les sudoku sans solution.... à compléter
        """
        self.fcreation_entree()
        self.fNouveau()
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                self.facile
                val=self.entree[i][j].get()
                if isValid(val):
                    val=int(val)
                else:
                    val=0
                tableau[i,j]=val
        # on resoud le sudoku
        mSudok = Sudoku(tableau)
        mSudok.solvee()
        
        # affiche quelque nombre pour le niveau
        f=0
        s=list()
        while f<32:
            i=randrange(9)
            j=randrange(9)
#            print "i = ",i, ", j = ",j
            if (i,j) not in s:
                    self.entree[i][j].set( str(int(mSudok.solution[i, j])))
                    tkinter.Entry(self.fenetre, textvariable=self.entree[i][j], width=2, font="Arial 30",state ='disabled',justify='center', validate='key', validatecommand=self.vcmd).grid(column=i, row=j)
                    f +=1
                    s.append((i,j))
        return
    
    def verif(self):
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                val=self.entree[i][j].get()
                if isValid(val):
                    val=int(val)
                else:
                    val=0
                tableau[i,j]=val
        mSudok = Sudoku(tableau)
        if mSudok.verification():
            messagebox.showinfo("Bien joué", "La grille est correcte pour l'instant :)")
        else:
            tkinter.messagebox.showerror("Erreur", "Une ou plusieur valeurs dupliquées")
            

    def dificile(self):
        """
        résoud le sudoku et affiche la solution
        ne gère pas les sudoku sans solution
        """
        self.fcreation_entree()
        self.fNouveau()
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                self.facile
                val=self.entree[i][j].get()
                if isValid(val):
                    val=int(val)
                else:
                    val=0
                tableau[i,j]=val
        # on resoud le sudoku
        mSudok = Sudoku(tableau)
        mSudok.solvee()
        
        # affiche quelque nombre pour le niveau
        f=0
        s=list()
        while f<24:
            i=randrange(9)
            j=randrange(9)
#            print "i = ",i, ", j = ",j
            if (i,j) not in s:
                    self.entree[i][j].set( str(int(mSudok.solution[i, j])))
                    tkinter.Entry(self.fenetre, textvariable=self.entree[i][j], width=2, font="Arial 30",state ='disabled',justify='center', validate='key', validatecommand=self.vcmd).grid(column=i, row=j)
                    f +=1
                    s.append((i,j))
        return
        
    # fenetre

    def __init__(self):
        """
        initialisation
        """        
        
        self.fenetre=Tk()
        self.fenetre.resizable(False, False)
        self.vcmd = (self.fenetre.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.fenetre.title("Sudoku")

        # barre des menu     
    
        self.menubar = Menu()

        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="Créer une Grille", command =self.fNouveau)
        self.menu3 = Menu(self.menu1, tearoff=0)
        self.menu3.add_command(label="Facile", command =self.facile)
        self.menu3.add_command(label="Moyen", command =self.moyen)
        self.menu3.add_command(label="Difficile", command =self.dificile)
        self.menu1.add_cascade(label="Nouvelle partie", menu=self.menu3)
        self.menu1.add_separator()
        self.menu1.add_command(label="Vérifier la Grille", command =self.verif)
        self.menu1.add_separator()
        self.menu1.add_command(label="Résoudre la Grille", command =self.fResoudre)
        self.menu1.add_separator()
        self.menu1.add_command(label="Quitter", command =self.fQuitter)
        self.menubar.add_cascade(label="Fichier", menu=self.menu1)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="A propos", command = self.info1)
        self.menu2.add_command(label="Régle de jeu", command =self.info2)
        self.menubar.add_cascade(label="Aide", menu=self.menu2)
    
        self.fenetre.protocol("WM_DELETE_WINDOW", self.fQuitter)
    
        self.fenetre.config(menu=self.menubar)   

        # creation des 9x9 cases
        self.fcreation_entree()

    
    def start(self):
        """
        lance le jeu
        """
        self.fenetre.mainloop()

                
    def fcreation_entree(self):
        """
        initialisation des entrees (Entry) et ajout a la fenetre
        """
        self.entree = []
        for i in range(9):
            self.entree+=[[]]
            for j in range(9):
                self.entree[i]+=[tkinter.StringVar()]
        for i in range(9):
            for j in range(9):
                if (i//3)%2 == (j//3)%2:
                    bcg="#33ff33"
                else:
                        bcg="#ffff33"
                if (self.entree[i][j].get()) == "":
                    c= tkinter.Entry(self.fenetre, textvariable=self.entree[i][j], width=2, font="Arial 30", bg=bcg,state ='normal',bd=5,justify='center', validate='key', validatecommand=self.vcmd)
                    c.grid(column=i, row=j)
                else:
                    c= tkinter.Entry(self.fenetre, textvariable=self.entree[i][j], width=2, font="Arial 30", bg=bcg,state ='disabled',justify='center', validate='key', validatecommand=self.vcmd)
                    bd=5, c.grid(column=i, row=j)
                self.entree[i][j].set("")
                
# ============================================================================
# Fonctions
# ============================================================================
def isValid(val):
    """
    test la valeur dans les cases
    - vrai si nombre entier entre 1 et 9
    - faux sinon
    """
    try:
        val=int(val)
        if val>0 and val<10:
            return True
        else:
            return False
    except:
        return False
# ============================================================================
# Programme
# ============================================================================

if __name__ == '__main__':
    Jeu=Interface()
    Jeu.start()
