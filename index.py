# Importation du module Tkinter pour créer une interface graphique
import tkinter as tk

# Fonction pour ajouter un caractère (chiffre ou opérateur) à l'affichage
def ajouter_caractere(caractere):
	affichage.insert(tk.END, caractere)

# Fonction pour effacer tout le contenu de l'affichage
def tout_effacer():
	affichage.delete(0, tk.END)

# Fonction pour effacer le dernier caractère de l'affichage
def effacer_un():
	texte = affichage.get()
	affichage.delete(0, tk.END)
	affichage.insert(0, texte[:-1])

# Fonction pour calculer le résultat de l'expression
def calculer():
	try:
		# On récupère le texte de l'affichage
		expression = affichage.get()
		# On utilise la fonction eval pour calculer le résultat
		resultat = eval(expression)
		# On affiche le résultat
		tout_effacer()
		affichage.insert(0, str(resultat))
	except Exception:
		# En cas d'erreur, on affiche 'Erreur'
		tout_effacer()
		affichage.insert(0, 'Erreur')

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title('Calculatrice')

# Création de l'affichage (Entry)
affichage = tk.Entry(fenetre, width=25, font=('Arial', 18), borderwidth=2, relief='solid', justify='right')
affichage.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Liste des boutons (chiffres et opérateurs)
boutons = [
	('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
	('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
	('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
	('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Création des boutons chiffres et opérateurs
for (texte, ligne, colonne) in boutons:
	if texte == '=':
		# Bouton égalité, lance le calcul
		bouton = tk.Button(fenetre, text=texte, width=5, height=2, font=('Arial', 16), command=calculer)
	else:
		# Les autres boutons ajoutent leur caractère à l'affichage
		bouton = tk.Button(fenetre, text=texte, width=5, height=2, font=('Arial', 16), command=lambda t=texte: ajouter_caractere(t))
	bouton.grid(row=ligne, column=colonne, padx=2, pady=2)

# Bouton pour tout effacer (C)
bouton_c = tk.Button(fenetre, text='C', width=5, height=2, font=('Arial', 16), command=tout_effacer, fg='red')
bouton_c.grid(row=5, column=0, padx=2, pady=2)

# Bouton pour effacer un caractère à la fois
bouton_efface_un = tk.Button(fenetre, text='⌫', width=5, height=2, font=('Arial', 16), command=effacer_un)
bouton_efface_un.grid(row=5, column=1, padx=2, pady=2)

# Bouton vide pour l'esthétique
bouton_vide1 = tk.Label(fenetre, width=5, height=2)
bouton_vide1.grid(row=5, column=2)

# Bouton vide pour l'esthétique
bouton_vide2 = tk.Label(fenetre, width=5, height=2)
bouton_vide2.grid(row=5, column=3)

# Boucle principale pour afficher la fenêtre
fenetre.mainloop()
