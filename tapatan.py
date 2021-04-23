#########################
# import des modules
import tkinter as tk

###########################
# constantes du programme
HAUTEUR=600
LARGEUR=600
HAUTEUR_LIGNE=400
LARGEUR_LIGNE=400
RAYON=10
color = 'black'
##########################
# fonctions du programme
def couleur_cercle(cercle):
    global color
    if color == 'black':
        color = 'blue'
    else:
        color = 'black'
    canvas.itemconfig(cercle, fill=color)

#############################
# programme principal
racine = tk.Tk()
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)

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
cercle_5 = canvas.create_oval(100 - RAYON, 500 - RAYON, 100 + RAYON, 500 + RAYON, fill="black")
cercle_6 = canvas.create_oval(300 - RAYON, 300 - RAYON, 300 + RAYON, 300 + RAYON, fill="black")
cercle_7 = canvas.create_oval(300 - RAYON, 500 - RAYON, 300 + RAYON, 500 + RAYON, fill="black")
cercle_8 = canvas.create_oval(500 - RAYON, 300 - RAYON, 500 + RAYON, 300 + RAYON, fill="black")
cercle_9 = canvas.create_oval(500 - RAYON, 500 - RAYON, 500 + RAYON, 500 + RAYON, fill="black")

canvas.tag_bind(cercle_1, "<1>", lambda cercle: couleur_cercle(cercle_1))
canvas.tag_bind(cercle_2, "<1>", lambda cercle: couleur_cercle(cercle_2))
canvas.tag_bind(cercle_3, "<1>", lambda cercle: couleur_cercle(cercle_3))
canvas.tag_bind(cercle_4, "<1>", lambda cercle: couleur_cercle(cercle_4))
canvas.tag_bind(cercle_5, "<1>", lambda cercle: couleur_cercle(cercle_5))
canvas.tag_bind(cercle_6, "<1>", lambda cercle: couleur_cercle(cercle_6))
canvas.tag_bind(cercle_7, "<1>", lambda cercle: couleur_cercle(cercle_7))
canvas.tag_bind(cercle_8, "<1>", lambda cercle: couleur_cercle(cercle_8))
canvas.tag_bind(cercle_9, "<1>", lambda cercle: couleur_cercle(cercle_9))

canvas.grid()

racine.mainloop()