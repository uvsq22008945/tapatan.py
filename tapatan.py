####################################################
# groupe MPCI 7
# Clément Coste
# Tom Le Goueff
# Yanis Kbayli
# Maeva Laurence
# Ghalayini Mohamad
# Sellier Benjamin
# https://github.com/uvsq22008945/tapatan.py.git
####################################################

import tkinter as tk
import tkinter.messagebox

###########################
# constantes du programme
HAUTEUR = 550
LARGEUR = 600
HAUTEUR_LIGNE = 400
LARGEUR_LIGNE = 400
RAYON = 10
cpt = 0
color = ['red', 'blue']
score_blue = 0
score_red = 0


##########################
# fonctions du programme
def initialiser_le_jeu():
    """
    Permet d'initialer le début du jeu.
    """

    global cercle_1, cercle_2, cercle_3, cercle_4, cercle_5
    global cercle_6, cercle_7, cercle_8, cercle_9, pion
    global compteur, success, pion_controlling, couleur_pion
    global liste, liste_deplacement, position

    if score_blue != 3 and score_red != 3:
        compteur = 0
        success = False
        pion_controlling = None
        couleur_pion = "black"
        position = None

        liste = [['black', "black", "black"],
                 ['black', "black", "black"],
                 ['black', "black", "black"]]

        liste_deplacement = [[], [], [], [], [], [], [], [], []]
        cercle_1 = canvas.create_oval(100 - RAYON, 100 - RAYON,
                                      100 + RAYON, 100 + RAYON, fill="black")
        cercle_2 = canvas.create_oval(300 - RAYON, 100 - RAYON,
                                      300 + RAYON, 100 + RAYON, fill="black")
        cercle_3 = canvas.create_oval(500 - RAYON, 100 - RAYON,
                                      500 + RAYON, 100 + RAYON, fill="black")
        cercle_4 = canvas.create_oval(100 - RAYON, 300 - RAYON,
                                      100 + RAYON, 300 + RAYON, fill="black")
        cercle_5 = canvas.create_oval(300 - RAYON, 300 - RAYON,
                                      300 + RAYON, 300 + RAYON, fill="black")
        cercle_6 = canvas.create_oval(500 - RAYON, 300 - RAYON,
                                      500 + RAYON, 300 + RAYON, fill="black")
        cercle_7 = canvas.create_oval(100 - RAYON, 500 - RAYON,
                                      100 + RAYON, 500 + RAYON, fill="black")
        cercle_8 = canvas.create_oval(300 - RAYON, 500 - RAYON,
                                      300 + RAYON, 500 + RAYON, fill="black")
        cercle_9 = canvas.create_oval(500 - RAYON, 500 - RAYON,
                                      500 + RAYON, 500 + RAYON, fill="black")
        pion = canvas.create_oval(20, 20, 50, 50, fill="blue")

        canvas.tag_bind(cercle_1, "<1>",
                        lambda cercle: couleur_cercle(cercle_1, 0, 0))
        canvas.tag_bind(cercle_2, "<1>",
                        lambda cercle: couleur_cercle(cercle_2, 0, 1))
        canvas.tag_bind(cercle_3, "<1>",
                        lambda cercle: couleur_cercle(cercle_3, 0, 2))
        canvas.tag_bind(cercle_4, "<1>",
                        lambda cercle: couleur_cercle(cercle_4, 1, 0))
        canvas.tag_bind(cercle_5, "<1>",
                        lambda cercle: couleur_cercle(cercle_5, 1, 1))
        canvas.tag_bind(cercle_6, "<1>",
                        lambda cercle: couleur_cercle(cercle_6, 1, 2))
        canvas.tag_bind(cercle_7, "<1>",
                        lambda cercle: couleur_cercle(cercle_7, 2, 0))
        canvas.tag_bind(cercle_8, "<1>",
                        lambda cercle: couleur_cercle(cercle_8, 2, 1))
        canvas.tag_bind(cercle_9, "<1>",
                        lambda cercle: couleur_cercle(cercle_9, 2, 2))
    else:
        if score_blue == score_red:
            message = "Le match est en égalité"
        elif score_blue > score_red:
            message = "Le pion bleu a gagné"
        else:
            message = "Le pion rouge a gagné"
        tkinter.messagebox.showinfo("success", message)


def couleur_cercle(cercle, x, y):
    """
    La fonction permet de définir le nombre de pion à poser qui est de 6 et
    permet le déplacement une fois la limite dépassée. Ajoute un message box
    à chaque victoire et renouvelle le score lors d'une victoire.
    """

    global color, cpt, liste, compteur, success
    global pion_controlling, couleur_pion, position
    global score_red, score_blue
    global liste_deplacement

    compteur += 1
    if liste[x][y] == "black" and compteur <= 6 and not success:
        cpt = (cpt + 1) % 2
        canvas.itemconfig(cercle, fill=color[cpt])
        liste[x][y] = color[cpt]
        canvas.itemconfig(pion, fill=color[(cpt + 1) % 2])
        if tableau():
            gagnant = liste[x][y]
            tkinter.messagebox.showinfo("success", gagnant+" Success unlocked")
            success = True
            if gagnant == "red":
                score_red += 1
            else:
                score_blue += 1
            c_zone.itemconfig(c_zone_compteur,
                              text=f"victoire\n  {score_blue} - {score_red}")
            initialiser_le_jeu()
    if compteur == 6:
        deplacement_possible()
    if compteur >= 6 and not success:
        if liste[x][y] == color[(cpt + 1) % 2]:
            pion_controlling, position = cercle, x * 3 + y
            couleur_pion = liste[x][y]
        else:
            if pion_controlling is not None:
                if x * 3 + y + 1 in liste_deplacement[position]:
                    canvas.itemconfig(pion_controlling, fill="black")
                    canvas.itemconfig(cercle, fill=couleur_pion)

                    liste[position // 3][position % 3] = "black"
                    liste[x][y] = couleur_pion
                    liste_deplacement = [[], [], [], [], [], [], [], [], []]
                    deplacement_possible()
                    pion_controlling = None

                    if tableau():
                        gagnant = liste[x][y]
                        tkinter.messagebox.showinfo(
                                "success", gagnant + " Success unlocked"
                        )
                        success = True
                        if gagnant == "red":
                            score_red += 1
                        else:
                            score_blue += 1
                        c_zone.itemconfig(
                                c_zone_compteur,
                                text=f"victoire\n  {score_blue} - {score_red}"
                        )
                        initialiser_le_jeu()

                    if liste[x][y] == couleur_pion:
                        cpt = (cpt + 1) % 2
                        canvas.itemconfig(pion, fill=color[(cpt + 1) % 2])


def tableau():
    """
    Cette fonction permet de reconnaître une victoire.
    """
    if (
        liste[0][0] == liste[0][1] == liste[0][2] != 'black' or
        liste[1][0] == liste[1][1] == liste[1][2] != 'black' or
        liste[2][0] == liste[2][1] == liste[2][2] != 'black' or
        liste[0][0] == liste[1][0] == liste[2][0] != 'black' or
        liste[0][1] == liste[1][1] == liste[2][1] != 'black' or
        liste[0][2] == liste[1][2] == liste[2][2] != 'black' or
        liste[0][0] == liste[1][1] == liste[2][2] != 'black' or
        liste[2][0] == liste[1][1] == liste[0][2] != 'black'
    ):
        return True
    return False


def deplacement_possible():
    """
    Permet de reconnaître les déplacements possibles.
    """

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
            (liste[1][2], 6),
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
            (liste[1][2], 6),
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
            (liste[2][1], 8)
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
    """
    Vérifie le code couleur des pions pour les déplacer.
    """
    for argument in args:
        if argument[0] == "black":
            liste_deplacement[i*3+j].append(argument[1])
    if liste[1][1] == "black":
        liste_deplacement[i*3+j].append(5)


#############################
# programme principal
racine = tk.Tk()
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)

# plateau
t_zone = tk.Canvas(racine, bg="white", height=50, width=600)
message = """
\nChacun des deux joueurs dispose de 3 jetons.
Le vainqueur est le premier joueur à aligner 3 de ses jetons sur le plateau.
"""
t_zone_Texte = t_zone.create_text(300, 20, text=message)
c_zone = tk.Canvas(racine, bg="white", height=50, width=600)
c_zone_compteur = c_zone.create_text(300, 20, text="victoire\n  0 - 0")

canvas.create_rectangle(100, 100, 500, 500, fill="#D3D2A5")

ligne_verticale = canvas.create_line(300, 100, 300, 500, fill="black")
ligne_horizontale = canvas.create_line(100, 300, 500, 300)

diagonal = canvas.create_line(100, 100, 500, 500)
diagonal = canvas.create_line(100, 500, 500, 100)

initialiser_le_jeu()

canvas.grid(row=1, column=0)
t_zone.grid(row=0, column=0)
c_zone.grid(row=3, column=0)

racine.mainloop()
