
# import : mot-clé pour importer un module
import tkinter as tk  # tk : module pour créer des interfaces graphiques


# def : mot-clé pour définir une fonction
def ajouter_caractere(caractere):  # caractere : paramètre de la fonction
	affichage.insert(tk.END, caractere)  # insert : ajoute à la fin de l'affichage


# Fonction pour effacer tout le contenu de l'affichage
def tout_effacer():
	affichage.delete(0, tk.END)  # delete : supprime tout le texte


# Fonction pour effacer le dernier caractère de l'affichage
def effacer_un():
	texte = affichage.get()  # get : récupère le texte actuel
	affichage.delete(0, tk.END)  # supprime tout
	affichage.insert(0, texte[:-1])  # insère le texte sauf le dernier caractère


# Fonction pour calculer le résultat de l'expression
def calculer():
	try:  # try : tente d'exécuter le code
		expression = affichage.get()  # récupère l'expression
		resultat = eval(expression)  # eval : calcule le résultat de l'expression
		tout_effacer()  # efface l'affichage
		affichage.insert(0, str(resultat))  # affiche le résultat
	except Exception:  # except : gère les erreurs
		tout_effacer()
		affichage.insert(0, 'Erreur')  # affiche 'Erreur' si problème


# Création de la fenêtre principale
fenetre = tk.Tk()  # tk.Tk() : crée la fenêtre
fenetre.title('Calculatrice')  # title : définit le titre de la fenêtre


# Création de l'affichage (Entry)
affichage = tk.Entry(fenetre, width=25, font=('Arial', 18), borderwidth=2, relief='solid', justify='right')  # Entry : zone de texte
affichage.grid(row=0, column=0, columnspan=4, padx=5, pady=5)  # grid : place l'affichage dans la fenêtre


# Liste des boutons (chiffres et opérateurs)
boutons = [  # liste de tuples (texte, ligne, colonne)
	('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
	('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
	('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
	('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]


# Création des boutons chiffres et opérateurs
for (texte, ligne, colonne) in boutons:  # boucle sur chaque bouton
	if texte == '=':
		bouton = tk.Button(fenetre, text=texte, width=5, height=2, font=('Arial', 16), command=calculer)  # bouton égalité
	else:
		bouton = tk.Button(fenetre, text=texte, width=5, height=2, font=('Arial', 16), command=lambda t=texte: ajouter_caractere(t))  # bouton chiffre ou opérateur
	bouton.grid(row=ligne, column=colonne, padx=2, pady=2)  # place le bouton dans la fenêtre


# Bouton pour tout effacer (C)
bouton_c = tk.Button(fenetre, text='C', width=5, height=2, font=('Arial', 16), command=tout_effacer, fg='red')  # bouton C
bouton_c.grid(row=5, column=0, padx=2, pady=2)  # place le bouton C


# Bouton pour effacer un caractère à la fois
bouton_efface_un = tk.Button(fenetre, text='⌫', width=5, height=2, font=('Arial', 16), command=effacer_un)  # bouton efface un caractère
bouton_efface_un.grid(row=5, column=1, padx=2, pady=2)


# Bouton vide pour l'esthétique
bouton_vide1 = tk.Label(fenetre, width=5, height=2)  # label vide
bouton_vide1.grid(row=5, column=2)


# Bouton vide pour l'esthétique
bouton_vide2 = tk.Label(fenetre, width=5, height=2)  # label vide
bouton_vide2.grid(row=5, column=3)


# Boucle principale pour afficher la fenêtre
fenetre.mainloop()  # mainloop : lance l'interface graphique