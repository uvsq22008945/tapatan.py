import tkinter as tk
import tkinter.messagebox

###########################
# constantes du programme
HAUTEUR = 600
LARGEUR = 600
HAUTEUR_LIGNE = 400
LARGEUR_LIGNE = 400
RAYON = 10
cpt = 0
color = ['red', 'blue']
compteur = 0

liste = [
    ['black', "black", "black"],
    ['black', "black", "black"],
    ['black', "black", "black"]
]

liste_deplacement = [[], [], [], [], [], [], [], [], []]


##########################
# fonctions du programme
def couleur_cercle(cercle, x, y):
    global color, cpt, liste, compteur
    if liste[x][y] == "black" and compteur < 6:
        cpt = (cpt + 1) % 2
        canvas.itemconfig(cercle, fill=color[cpt])
        liste[x][y] = color[cpt]
        if tableau() and compteur != 6:
            gagnant = liste[x][y]
            tkinter.messagebox.showinfo("success", gagnant+" Success unlocked")
        compteur += 1
    if compteur == 6:
        deplacement()
        print(liste_deplacement)


def tableau():

    if (    liste[0][0] == liste[0][1] == liste[0][2] != 'black' or # première ligne
            liste[1][0] == liste[1][1] == liste[1][2] != 'black' or # deuxième ligne
            liste[2][0] == liste[2][1] == liste[2][2] != 'black' or # troisième ligne
            liste[0][0] == liste[1][0] == liste[2][0] != 'black' or # première colonne
            liste[0][1] == liste[1][1] == liste[2][1] != 'black' or # deuxième colonne
            liste[0][2] == liste[1][2] == liste[2][2] != 'black' or # troisième colonne
            liste[0][0] == liste[1][1] == liste[2][2] != 'black' or # première diagonale
            liste[2][0] == liste[1][1] == liste[0][2] != 'black' # deuxième diagonale
        ): 
        return True
    return False


def deplacement():

    if liste[0][0] != "black":
        deplacement_append(
            0, 0, 
            (liste[0][1], 2),
            (liste[1][0], 4),
        )
    if liste[0][1] != "black":
            deplacement_append(
            0, 1, 
            (liste[0][0], 1),
            (liste[0][2], 3),
        )
    if liste[0][2] != "black":
            deplacement_append(
            0, 2, 
            (liste[0][1], 2),
            (liste[0][2], 3),
        )
    if liste[1][0] != "black":
            deplacement_append(
            1, 0, 
            (liste[0][0], 1),
            (liste[2][0], 7),
        )
    if liste[1][1] != "black":
            deplacement_append(
            1, 1, 
            (liste[0][0], 1),
            (liste[0][1], 2),
            (liste[0][2], 3),
            (liste[1][0], 4),
            (liste[1][0], 6),
            (liste[2][0], 7),
            (liste[2][1], 8),
            (liste[2][2], 9)
        )
    if liste[1][2] != "black":
            deplacement_append(
            1, 2, 
            (liste[0][2], 3),
            (liste[2][2], 9)
        )
    if liste[2][0] != "black":
            deplacement_append(
            2, 0, 
            (liste[1][0], 4),
            (liste[2][0], 7)
        )
    if liste[2][1] != "black":
            deplacement_append(
            2, 1, 
            (liste[2][0], 7),
            (liste[2][2], 9)
        )
    if liste[2][2] != "black":
            deplacement_append(
            2, 2, 
            (liste[1][2], 6),
            (liste[2][1], 8),
        )


def deplacement_append(i, j, *args):
    for argument in args:
        if argument[0] == "black":
            liste_deplacement[i*3+j].append(argument[1])
    if liste[1][1] == "black":
        liste_deplacement[i*3+j].append(5)



#############################
# programme principal
racine = tk.Tk()
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
canvas.grid()

# plateau
canvas.create_rectangle(100, 100, 500, 500, fill="#D3D2A5")

ligne_verticale = canvas.create_line(300, 100, 300, 500, fill="black")
ligne_horizontale = canvas.create_line(100, 300, 500, 300)

diagonal = canvas.create_line(100, 100, 500, 500)
diagonal = canvas.create_line(100, 500, 500, 100)

cercle_1 = canvas.create_oval(100 - RAYON, 100 - RAYON, 100 + RAYON, 100 + RAYON, fill="black")
cercle_2 = canvas.create_oval(300 - RAYON, 100 - RAYON, 300 + RAYON, 100 + RAYON, fill="black")
cercle_3 = canvas.create_oval(500 - RAYON, 100 - RAYON, 500 + RAYON, 100 + RAYON, fill="black")
cercle_4 = canvas.create_oval(100 - RAYON, 300 - RAYON, 100 + RAYON, 300 + RAYON, fill="black")
cercle_5 = canvas.create_oval(300 - RAYON, 300 - RAYON, 300 + RAYON, 300 + RAYON, fill="black")
cercle_6 = canvas.create_oval(500 - RAYON, 300 - RAYON, 500 + RAYON, 300 + RAYON, fill="black")
cercle_7 = canvas.create_oval(100 - RAYON, 500 - RAYON, 100 + RAYON, 500 + RAYON, fill="black")
cercle_8 = canvas.create_oval(300 - RAYON, 500 - RAYON, 300 + RAYON, 500 + RAYON, fill="black")
cercle_9 = canvas.create_oval(500 - RAYON, 500 - RAYON, 500 + RAYON, 500 + RAYON, fill="black")

canvas.tag_bind(cercle_1, "<1>", lambda cercle: couleur_cercle(cercle_1, 0, 0))
canvas.tag_bind(cercle_2, "<1>", lambda cercle: couleur_cercle(cercle_2, 0, 1))
canvas.tag_bind(cercle_3, "<1>", lambda cercle: couleur_cercle(cercle_3, 0, 2))
canvas.tag_bind(cercle_4, "<1>", lambda cercle: couleur_cercle(cercle_4, 1, 0))
canvas.tag_bind(cercle_5, "<1>", lambda cercle: couleur_cercle(cercle_5, 1, 1))
canvas.tag_bind(cercle_6, "<1>", lambda cercle: couleur_cercle(cercle_6, 1, 2))
canvas.tag_bind(cercle_7, "<1>", lambda cercle: couleur_cercle(cercle_7, 2, 0))
canvas.tag_bind(cercle_8, "<1>", lambda cercle: couleur_cercle(cercle_8, 2, 1))
canvas.tag_bind(cercle_9, "<1>", lambda cercle: couleur_cercle(cercle_9, 2, 2))

boutton_joueur = tk.Button(racine, text = "HUMAIN VS IA")
boutton_robot = tk.Button(racine, text = "IA VS IA")

boutton_joueur.grid(column = 0, row = 2)
boutton_robot.grid(row = 3)

racine.mainloop()