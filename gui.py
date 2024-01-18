from tkinter import *
from tkinter import messagebox

def nyi():
    msg = messagebox.showinfo("Erreur dans la matrice", "Pas ecnore implémenté\n Revenez plus tard ;)")

main = Tk()
main.title("RT2@hacker")
main.geometry("400x250")
main.resizable(False,False)
bienvenue = Label(main, text="Bienvenue, quelle attaque voulez-vous utiliser ?")
bienvenue.place(x=80, y=10)
button = Button(main, text="DHCP",width=10)
button.place(x=85, y=75)
button = Button(main, text="STP",width=10)
button.place(x=85, y=125)
button = Button(main, text="NYI",width=10,command=nyi)
button.place(x=225, y=75)
button = Button(main, text="NYI",width=10,command=nyi)
button.place(x=225, y=125)
button = Button(main, text="INFOS",width=10)
button.place(x=150, y=175)
main.mainloop()


